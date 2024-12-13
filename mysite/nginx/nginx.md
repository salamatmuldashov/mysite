1. **Load Balancing**:
   - Nginx was chosen as a load balancer.
   - Round-robin method were implemented

2. **Create or Modify the Nginx Configuration File**:
   The  configuration file is  located at `mysite/nginx/nginx.conf`.

3. **Define the Upstream Block**:
   In the configuration file, define an `upstream` block that specifies the backend servers. This block will handle the distribution of incoming requests to the servers.

4. **Set Up a Server Block to Handle Requests**:
   The `server` block in the Nginx configuration file specifies how requests should be handled. You will proxy incoming requests to the upstream group defined earlier

