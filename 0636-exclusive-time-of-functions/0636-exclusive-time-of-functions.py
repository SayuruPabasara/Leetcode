class Solution(object):
    def exclusiveTime(self, n, logs):
        result = [0] * n
        stack = []
        prevTime = 0

        for log in logs:
            fid, typ, time = log.split(":")
            fid = int(fid)
            time = int(time)

            if typ == "start":
                if stack:
                    result[stack[-1]] += time - prevTime
                stack.append(fid)
                prevTime = time
            else:  # "end"
                result[stack.pop()] += time - prevTime + 1
                prevTime = time + 1

        return result