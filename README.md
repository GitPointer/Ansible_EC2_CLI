 #  ANSIBLE CLI-User Manual
 ## Installation on Ansible Master Node
 
 >**Note:**  All installation instructions are specific to **`[Ubuntu Server 18.04 LTS (HVM), SSD Volume Type - ami-0dc8d444ee2a42d8a (64-bit x86) / ami-0c7316a2d5e1a85a1 (64-bit Arm)]`**
 
 1. **Prerequisite**
       1. Running  EC2 instance **`[Ubuntu Server 18.04 LTS (HVM), SSD Volume Type - ami-0dc8d444ee2a42d8a (64-bit x86) / ami-0c7316a2d5e1a85a1 (64-bit Arm)]`**
       2. Security groups having `SSH permission`
       
       >**Note:**  This **Security group ID**  further need to set in `Ansible_EC2/ec2-vars/webservers.yml`
       
 3. **Install python 2.7**
 
        >sudo apt-get install python-dev build-essential
         
       >**Note:**  Probably need to also:
        
        >sudo apt-get update --fix-missing
  
 4.   **Install boto**
 
          > sudo apt-get install python-pip
          > pip install boto
          
 5.   **Install Ansible**
          
          >sudo apt-get update
          >sudo apt-get install software-properties-common
          >sudo apt-add-repository ppa:ansible/ansible
          >sudo apt-get update
          >sudo apt-get install ansible 
          
 ## Configuration
 1.  **Add AWS Private Key:**
 
         >vi ~/.ssh/id_rsa
        
       >  Copy entire contents of the .pem file into id_rsa.To save and exit: press “Esc” then enter “:wq!”
 2.  **Add AWS Public Key:**
          
          >vi ~/.ssh/id_rsa.pub

      >  Open the .ppk private key in puttygen or in other tool, copy the public key to the clipboard, and place into id_rsa.pub.
                                     

> **Note**   Add read/write privileges
   
    >chmod 0600 ~/.ssh/id*
     
 3.  **Authentication:**
 Authentication on AWS-related modules is handled by specifying the access and private key as ENV variables
     
     **For environment variables:**
     
         >export AWS_ACCESS_KEY_ID='<Your_ACCESS_KEY_ID>'
     
         >export AWS_SECRET_ACCESS_KEY='<Your_AWS_SECRET_ACCESS_KEY>'
   
       > **Note**   You can also add environment variables permanently as below
      >`vi ~/.bash_profile'`
     
        **Add below in file. To save and exit: press “Esc” then enter “:wq!”**
     
          >export AWS_ACCESS_KEY_ID='<Your_ACCESS_KEY_ID>'
        
          >export AWS_SECRET_ACCESS_KEY='<Your_AWS_SECRET_ACCESS_KEY>'

 4.  **Copy  `Ansible_EC2` and Permission Setting**
      1. Copy the `Ansible_EC2` from local to Master node using winscp or any other tool.
      2. Go to root dir  `Ansible_EC2` 
      3.  Run below command
			  > `chmod +x ec2.py`
			  > `chmod +x ec2.ini`
	 4. Go to root dir  `/etc/ansible/` 
      5.  Run below command
			  > `sudo chmod 700 hosts`
 5.  Config parameters defined in **`Ansible_EC2/ec2-vars/webservers.yml`**
      1. ec2_instance_type **(default `t2.micro`)**
      2. ec2_image **(default `ami-0dc8d444ee2a42d8a`)**
      3. ec2_region **(default `eu-west-1`)**
      4. ec2_tag_Name **(default`AnsibleHost`)**
      5. ec2_tag_Type **(default`webserver`)**
      6. ec2_security_grp 
      7. ec2_keypair
      8. ec2_tag_Environment **(default`testing`)**
      9. aws_access_key
      10. aws_secret_key
      11. ec2_volume_size **(default`8GB`)**
   6.  Config parameters defined in **`Ansible_EC2/AnsibleCLI.py`**
       1. **host_group** for dynamic inventory **(default `tag_Type_webserver`)**
      
 ## RUN		      
 1. **Run Ansible Playbook**
 
    >**Note:**  Do the `SSH`  to Ansible Master Node 
    
    - Go to root dir  `Ansible_EC2`  under `/home/ubuntu`
  
       ![enter image description here](https://raw.githubusercontent.com/GitPointer/ec2_ansible/main/ansible_master_pwd.png)


    - Run below command
			 > `python AnsibleCLI.py`
     - Below Menu will be display for option selection 

   	   ![[Press between 1-5] : for launch the specified number of AWS EC2 t2.micro (Free-Tier) instances.[Press 6] :           for installing Apache on AWS EC2 t2.micro (Free-Tier) instances.[Press <9> to exit]>>>](https://raw.githubusercontent.com/GitPointer/ec2_ansible/main/playbook_run.png)	
    
    - Execution Result
 ![enter image description here](https://raw.githubusercontent.com/GitPointer/ec2_ansible/main/playbook_run_result.png)




