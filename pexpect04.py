import pexpect

# start a child process with spawn
# this process waits for the input
#form user


child = pexpect.spawn("cat")

#the input to the cat process is sent
#by the send line()
child.sendline("Welcome World")

#prints the index of matched string
#expressing with child process

print(child.expect(["Hello", "Welcome World"],timeout=120))