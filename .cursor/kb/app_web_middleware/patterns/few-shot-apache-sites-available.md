# Few-shot — Apache `sites-available` (Debian/Ubuntu)

> **Propósito**: *VirtualHost* **completo** HTTP→HTTPS + `mod_proxy` para *upstream*. Revisão única antes de copiar para PRD.  
> **MCP validado**: não aplicável

## Quando usar

- `a2enmod ssl proxy proxy_http headers rewrite`
- Arquivos em `/etc/apache2/sites-available/` + `a2ensite app-api`

## Arquivo sugerido: `/etc/apache2/sites-available/app-api.conf`

```apache
<IfModule mod_ssl.c>
<VirtualHost *:443>
    ServerName api.exemplo.internal

    SSLEngine on
    SSLCertificateFile      /etc/ssl/certs/api.exemplo.internal.crt
    SSLCertificateKeyFile   /etc/ssl/private/api.exemplo.internal.key
    # SSLCertificateChainFile /etc/ssl/certs/api.exemplo.internal-chain.crt

    ProxyPreserveHost On
    RequestHeader set X-Forwarded-Proto "https"
    RequestHeader set X-Forwarded-Port "443"

    # Limites — alinhar à API
    LimitRequestBody 26214400

    ProxyPass        / http://127.0.0.1:3000/
    ProxyPassReverse / http://127.0.0.1:3000/

    Header always set X-Content-Type-Options "nosniff"

    ErrorLog ${APACHE_LOG_DIR}/app-api-ssl-error.log
    CustomLog ${APACHE_LOG_DIR}/app-api-ssl-access.log combined
</VirtualHost>
</IfModule>

<VirtualHost *:80>
    ServerName api.exemplo.internal
    RewriteEngine On
    RewriteRule ^ https://%{HTTP_HOST}%{REQUEST_URI} [END,NE,R=permanent]
</VirtualHost>
```

## Activar

```bash
sudo a2ensite app-api
sudo apache2ctl configtest && sudo systemctl reload apache2
```

## Ver também

- [../concepts/apache-httpd-linux.md](../concepts/apache-httpd-linux.md)
- [reverse-proxy-upstream.md](reverse-proxy-upstream.md)
