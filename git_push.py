import subprocess


def execute_cmd(cmd):
    process = subprocess.Popen(cmd, shell=True, stdout = subprocess.PIPE, universal_newlines=True)
    stdout,stderr = process.communicate()
    print("output: {}".format(stdout))
    print("error:".format(stderr))

execute_cmd("df -h")
execute_cmd("ls -l")

execute_cmd("git add .")
execute_cmd('git commit -am "updated reports"')
execute_cmd("git push https://grthilak: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@github.com/grthilak/mspoctest1.git")
