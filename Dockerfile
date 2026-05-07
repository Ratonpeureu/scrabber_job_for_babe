FROM python:3.11-slim

#Update Your DockerFile for add your path//
# Install pandas // 
# You cann //
RUN pip install --no-cache-dir pandas

# Copier le ##//CSV et CV//
# For Exemmple 

#COPY CV_Awa_Ndiaye_Ba_.pdf /data/CV_Awa_Ndiaye_Ba_.pdf
#Copy Brute CSV after first extract// for exemple// 
#COPY emploidakar_offres_emails.csv /data/emploidakar_offres_emails.csv
#Finaly copy cleaned csv// for exemple  
#COPY emploidakar_offres_emails.csv /data/emploidakar_offres_emails.csv


WORKDIR /data


#Define final csv path after//extract email//and after cleaned CSV///
#defien commande CMD For run
#for exemple

#CMD ["python", "send_mail_from_csv.py"]
