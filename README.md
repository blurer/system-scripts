# System Scripts

install requirements.txt, alias your .zshrc or bashrc


System Info

```
$ ./sysinfo.py
┏━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Item                 ┃ Value                                       ┃
┡━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┩
│ cpu_model            │ AMD Ryzen 3 3200G with Radeon Vega Graphics │
│ cores_threads        │ 4c / 4t                                     │
│ system_memory        │ 4.5Gi / 47Gi / 60Gi                         │
│ disk_storage         │ 29G / 840G / 915G                           │
│ uptime               │ up 9 hours, 31 minutes                      │
│ os_name              │ Arch Linux                                  │
└──────────────────────┴─────────────────────────────────────────────┘
```


Docker Info

```
$ ./docker_info.py
┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━┓
┃ Name         ┃ Status                        ┃ Ports                                                                                                                 ┃ Networks               ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━┩
│ hoarder-mei… │ Up 11 hours                   │ 7700/tcp                                                                                                              │ hoarder_default        │
│ hoarder-web… │ Up 11 hours (healthy)         │ 0.0.0.0:2323->3000/tcp, [::]:2323->3000/tcp                                                                           │ hoarder_default        │
│ hoarder-chr… │ Up 11 hours                   │                                                                                                                       │ hoarder_default        │
│ wiki         │ Up 11 hours                   │ 80/tcp, 0.0.0.0:7005->443/tcp, [::]:7005->443/tcp                                                                     │ proxy_default          │
│ beszel       │ Up 11 hours                   │ 0.0.0.0:8090->8090/tcp, :::8090->8090/tcp                                                                             │ beszel_default         │
│ beszel-agent │ Up 11 hours                   │                                                                                                                       │ host                   │
│ root-startp… │ Up 11 hours                   │ 0.0.0.0:6005->80/tcp, [::]:6005->80/tcp                                                                               │ root-startpage_default │
│ resume-open… │ Exited (0) 11 hours ago       │                                                                                                                       │ resume_default         │
│ flightlog-j… │ Up 11 hours                   │ 0.0.0.0:3420->3000/tcp, [::]:3420->3000/tcp                                                                           │ flightlog_default      │
│ whoogle-sea… │ Exited (137) 11 hours ago     │                                                                                                                       │ proxy_default          │
│ portainer    │ Up 11 hours                   │ 8000/tcp, 9443/tcp, 0.0.0.0:9000->9000/tcp, :::9000->9000/tcp                                                         │ proxy_default          │
│ uptime-kuma  │ Up 11 hours (healthy)         │ 0.0.0.0:7006->3001/tcp, [::]:7006->3001/tcp                                                                           │ proxy_default          │
│ proxy-app-1  │ Up 11 hours                   │ 0.0.0.0:80->80/tcp, :::80->80/tcp, 0.0.0.0:443->443/tcp, :::443->443/tcp, 0.0.0.0:8181->81/tcp, [::]:8181->81/tcp     │ proxy_default          │
│ tasks.md     │ Up 11 hours                   │ 0.0.0.0:3333->8080/tcp, [::]:3333->8080/tcp                                                                           │ proxy_default          │
│ glance-glan… │ Up 11 hours                   │ 0.0.0.0:8727->8080/tcp, [::]:8727->8080/tcp                                                                           │ proxy_default          │
│ cloudflare-… │ Up 11 hours                   │                                                                                                                       │ host                   │
│ watchtower   │ Restarting (0) 35 seconds ago │                                                                                                                       │ bridge                 │
│ mealie       │ Up 11 hours (healthy)         │ 0.0.0.0:9925->9000/tcp, [::]:9925->9000/tcp                                                                           │ proxy_default          │
│ openspeedte… │ Up 11 hours                   │ 0.0.0.0:3000-3001->3000-3001/tcp, :::3000-3001->3000-3001/tcp, 8080/tcp                                               │ bridge                 │
│ pihole       │ Up 11 hours (healthy)         │ 0.0.0.0:53->53/tcp, 0.0.0.0:53->53/udp, :::53->53/tcp, :::53->53/udp, 67/udp, 0.0.0.0:8088->80/tcp, [::]:8088->80/tcp │ proxy_default          │
└──────────────┴───────────────────────────────┴───────────────────────────────────────────────────────────────────────────────────────────────────────────────────────┴────────────────────────┘
```

IP Info

```
# ./ip.py
┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┓
┃ Field        ┃ Value          ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━┩
│ IP           │ x.x.x.x        │
│ ASN          │ AS5650         │
│ asn_org      │ FRONTIER-FRTR  │
└──────────────┴────────────────┘
```


(same as ip, but with tailscale ip and asn org info)


```
$ ./ip2.py
┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━┓
┃ Field        ┃ Value          ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━┩
│ Public IP    │ x.x.x.x        │
│ ASN          │ AS5650         │
│ ASN Org      │ FRONTIER-FRTR  │
│ Tailscale IP │ 100.100.10.10  │
└──────────────┴────────────────┘
```
