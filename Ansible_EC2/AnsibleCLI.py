import os
import pprint
import subprocess
import sys


class AnsibleCLI:

    def __init__(self):
        self.host_group = "tag_Type_webserver"
        self.ec2_inv = "localhost"
        self.apache_inv = "ec2.py"
        self.ec2_playbook = "launch_ec2.yml"
        self.apache_playbook = "install_apache.yml"
        self.timeout = "300"

    def install_apache(self):
        cmd = ["ansible-playbook",
               "-i{}".format(self.apache_inv),
               "-e host_group={}".format(self.host_group),
               "-e ANSIBLE_HOST_KEY_CHECKING=False",
               "{}".format(self.apache_playbook),
               "-v"]
        proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

        try:
            if sys.version_info > (3, 0):
                # Python 3 code in this block
                outs, errs = proc.communicate(timeout=self.timeout)
                pprint.pprint(outs.decode().strip().split('\n'))
            else:
                # Python 2 code in this block
                outs, errs = proc.communicate()
                pprint.pprint(outs.decode().strip().split('\n'))
            return True
        except subprocess.SubprocessError as errs:
            proc.kill()
            sys.exit("install_apache Error: {}".format(errs))

    def launch_ec2(self, count):
        cmd = ["ansible-playbook",
               "-i {},".format(self.ec2_inv),
               "-e count={} host_group={}".format(count, self.host_group),
               "-e ANSIBLE_HOST_KEY_CHECKING=False",
               "{}".format(self.ec2_playbook),
               "-v"]
        proc = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE)

        try:
            if sys.version_info > (3, 0):
                # Python 3 code in this block
                outs, errs = proc.communicate(timeout=self.timeout)
                pprint.pprint(outs.decode().strip().split('\n'))
            else:
                # Python 2 code in this block
                outs, errs = proc.communicate()
                pprint.pprint(outs.decode().strip().split('\n'))
            return True
        except subprocess.SubprocessError as errs:
            proc.kill()
            sys.exit("launch_ec2 Error: {}".format(errs))

    def run(self):
        # Main method
        while True:
            try:
                print("********************************************************************")
                ec2_count = input(
                    '{:<20}'.format('[Press between 1-5]') + ":for launch the specified number of AWS EC2 t2.micro ("
                                                             "Free-Tier) instances.\n"
                    + '{:<20}'.format('[Press 6]') + ":for installing Apache on AWS EC2 t2.micro (Free-Tier) "
                                                     "instances.\n["
                                                     "Press <9> to exit]>>>")
                if int(ec2_count) == 9:
                    break;
                elif 1 <= int(ec2_count) <= 5:
                    if self.launch_ec2(ec2_count):
                        self.install_apache()
                elif int(ec2_count) == 6:
                    self.install_apache()
                elif ec2_count is not None and len(ec2_count) != 0:
                    print("Error::Wrong Input:{}".format(ec2_count))
            except Exception as e:
                print(e)
        print("********************************************************************")


if __name__ == "__main__":
    try:
        AnsibleCLI().run()
    except KeyboardInterrupt as error:
        print(error)
    except Exception as e:
        print(e)
