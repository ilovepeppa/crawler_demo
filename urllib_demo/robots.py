from urllib.robotparser import RobotFileParser

rp = RobotFileParser()
rp.set_url('http://www.jianshu.com/robots.txt')
rp.read()
print(rp.can_fetch('*', 'https://www.jianshu.com/p/07296c957d5e'))
print(rp.can_fetch('*', 'http://www.jianshu.com/search?q=python&page=1&type=collections'))

nums = [0, 1, 0, 3, 12]
i = 0
j = len(nums) - 1
while i < j:
    if nums[i] == 0:
        nums.append(nums[i])
        del nums[i]
        j -= 1
    else:
        i += 1

print(nums)
