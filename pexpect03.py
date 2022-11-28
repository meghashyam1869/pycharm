import pexpect

# start a child process with spawn
# it just  echos geeksforgeeks

child = pexpect.spawn("echo myworld")

print(child.expect(["Hello", "welcome", "myworld"]))