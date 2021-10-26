from enum import Enum
"""
Interview problem : design a json parser from scratch:
    It is coming from untrusted source (meaning validation of json is required)
    the key will always be string the value can be string or another key value pair.
    Sample input {'abc':{'d':'ef','r':'er'}} -- map.get("abc").get("d") should return "ef".
    No other type i.e. integer or boolean or array in the json
    Validation and parsing must in done simultaneously
    In case of invalid json string throw exception
"""

class State(Enum):
    OPEN = 1
    KEY = 2
    VALUE = 3
    CLOSE = 4

class JsonParser:
    def remove_whilespace(self):
        while self.index < self.length and self.input[self.index] == ' ':
            self.index += 1

    def get_word(self):
        ans = ''
        prev = self.input[self.index]
        self.index += 1
        while self.index < self.length and self.input[self.index] != prev:
            ans += self.input[self.index]
            self.index += 1
        if self.input[self.index] == prev:
            self.index += 1
        return ans

    def recursive(self):
        state = State.OPEN
        res = {}
        stop = False
        while self.index < self.length:
            self.remove_whilespace()
            cur = self.input[self.index]
            if state == State.OPEN:
                if cur != '{':
                    raise RuntimeError("We need to open with '{', but get : {0} instead.".format(cur))
                state = State.KEY
            elif state == State.KEY:
                if cur not in ['\'', '"']:
                    raise RuntimeError("We need to extract key which starts from ' or \", but get {0} instead.".format(cur))
                pending_key = self.get_word()
                self.remove_whilespace()
                nxt = self.input[self.index]
                if nxt != ':':
                    raise RuntimeError("We need ':' to move to VALUE state, but get {0} instead.".format(nxt))
                state = state.VALUE
            elif state == State.VALUE:
                if cur in ['"', "'"]:
                    res[pending_key] = self.get_word()
                    pending_key = None
                elif cur == "{":
                    res[pending_key] = self.recursive()
                else:
                    raise RuntimeError("We need to get string value which starts from ' or \" or child dict object, but get {0} instead.".format(cur))
                self.remove_whilespace()
                nxt = self.input[self.index]
                if nxt == ',':
                    state = State.KEY
                elif nxt == '}':
                    state = State.CLOSE
                else:
                    raise RuntimeError("We need to get ',' to get next key-value pair or '}' to stop and return result., but get {0} instead.".format(nxt))
            elif state == State.CLOSE:
                stop = True
            else:
                raise RuntimeError("Unknow state.")
            if stop:
                break
            self.index += 1
        return res

    def parse(self, input):
        self.input = input
        self.index = 0
        self.length = len(input)
        res = self.recursive()
        if self.index != self.length:
            raise RuntimeError("Can't traverse all chars and stops at index : {0} . ".format(self.index))
        return res

if __name__ == "__main__":
    jsonParser = JsonParser()
    print(jsonParser.parse("{\"abc\":{\"bcde\":\"fg\",\"xml\":\"asd\"}}"))
    # print(jsonParser.parse("{\"zabc\":{zbcde\":\"fg\",\"xml\":\"asd\"}}"))
    # print(jsonParser.parse("{{\"abc\":{\"zbcde\":\"fg\",\"xml\":\"asd\"}}"))
    print(jsonParser.parse("{\"abc\":{\"zbcde\":\"fg\",\"xml\":\"asd\"}}}"))

