class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        strs = ""
        for i in range(len(command)):
            if command[i] == "G":
                strs += "G"
            elif command[i] == "(" and command[i+1] == ")":
                strs += "o"
            elif command[i] == "(" and command[i+1] == "a" and command[i+2] =="l" and command[i+3] ==")":
                strs += "al"
        return strs