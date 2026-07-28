Write-Host "SECURITY HARDENING - Starting..."

# 1. USERS
Write-Host "[1/5] Creating local users..."
try { New-LocalUser -Name "guest_user" -Password (ConvertTo-SecureString "Guest123!" -AsPlainText -Force) -FullName "Guest User" -ErrorAction Stop; Write-Host "guest_user created" } catch { Write-Host "guest_user already exists" }
try { New-LocalUser -Name "dev_user" -Password (ConvertTo-SecureString "Dev123!" -AsPlainText -Force) -FullName "Dev User" -ErrorAction Stop; Write-Host "dev_user created" } catch { Write-Host "dev_user already exists" }
try { Add-LocalGroupMember -Group "Administrateurs" -Member "dev_user" -ErrorAction Stop; Write-Host "dev_user added to Admins" } catch { Write-Host "dev_user already in Admins" }

# 2. FOLDERS
Write-Host "[2/5] Creating secure folders..."
New-Item -ItemType Directory -Path "C:\SecureFolders\Admin" -Force | Out-Null
New-Item -ItemType Directory -Path "C:\SecureFolders\Dev" -Force | Out-Null
New-Item -ItemType Directory -Path "C:\SecureFolders\Guest" -Force | Out-Null
Write-Host "Folders created"

# 3. FIREWALL
Write-Host "[3/5] Configuring firewall..."
try { New-NetFirewallRule -DisplayName "Block FTP" -Direction Inbound -Protocol TCP -LocalPort 21 -Action Block -ErrorAction Stop | Out-Null; Write-Host "FTP blocked" } catch { Write-Host "FTP rule exists" }
try { New-NetFirewallRule -DisplayName "Block Telnet" -Direction Inbound -Protocol TCP -LocalPort 23 -Action Block -ErrorAction Stop | Out-Null; Write-Host "Telnet blocked" } catch { Write-Host "Telnet rule exists" }
try { New-NetFirewallRule -DisplayName "Allow Flask API" -Direction Inbound -Protocol TCP -LocalPort 5000 -Action Allow -ErrorAction Stop | Out-Null; Write-Host "Flask API allowed" } catch { Write-Host "Flask rule exists" }

# 4. AUDIT
Write-Host "[4/5] Configuring audit logging..."
AuditPol /set /subcategory:"Logon" /success:enable /failure:enable | Out-Null
AuditPol /set /subcategory:"File System" /success:enable /failure:enable | Out-Null
Write-Host "Audit logging configured"

# 5. SERVICES
Write-Host "[5/5] Disabling unused services..."
Disable-WindowsOptionalFeature -Online -FeatureName "TelnetClient" -NoRestart | Out-Null
Write-Host "Telnet disabled"

Write-Host "SECURITY HARDENING COMPLETE!"