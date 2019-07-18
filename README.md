# Getting started
1. Generate new certificates:
  * Generate a certificate using the quinn-reverse-proxy utility:
  ```
  $ docker run -it --rm -v $(pwd)/certs:/usr/src/quinn-reverse-proxy/certs --name proxy --entrypoint generate-cert quinn-reverse-proxy:latest
  ```
  * Or, optionally, use `openssl` or another tool to generate the certificates.
  ```
  $ mkdir certs
  $ openssl ...
  $ mv <<certificate file>> certs/cert.der
  $ mv <<key file>> certs/key.der
  ```

2. Run the system: `docker-compose up`