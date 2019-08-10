# Installing Dependencies
sudo apt install -y python3.7
sudo apt install -y git
sudo apt install -y openjdk-8-jre
sudo apt install -y vim

# Copy the content
sudo mkdir /opt/MCSS
sudo cp -r * /opt/MCSS

# Copy to bin
sudo cp /opt/MCSS/MCSS /usr/bin

# Install BuildTools
cd /opt/MCSS/bukkit
sudo wget https://hub.spigotmc.org/jenkins/job/BuildTools/lastSuccessfulBuild/artifact/target/BuildTools.jar

# Get authorisations
chmod 777 /usr/bin/MCSS
chmod 777 -R /opt/MCSS
