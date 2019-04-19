# pioTrackerPWA

To run with docker: docker run -d --name bus -p 80:80 bus

At the moment, apiv0.5 in the backend folder is the most stable image, and involves running the parsing script with every request. apiv1 has some stuff which should make requests faster, but ran a background script that ended up crashing the server with time. I'll look into a better API caching system later. 