@echo off
echo ============================================
echo    AUTOMATIC BACKUP - %date% %time%
echo ============================================

set SOURCE_PC0=C:\Users\malik\Desktop\log-analysis\Clients\PC0
set SOURCE_PC1=C:\Users\malik\Desktop\log-analysis\Clients\PC1
set SOURCE_PC2=C:\Users\malik\Desktop\log-analysis\Clients\PC2
set BACKUP=C:\Users\malik\Desktop\log-analysis\Backup
set LOG=C:\Users\malik\Desktop\log-analysis\Backup\backup_log.txt

echo.
echo [1/3] Backing up PC0...
robocopy %SOURCE_PC0% %BACKUP%\PC0 /E /LOG+:%LOG%

echo.
echo [2/3] Backing up PC1...
robocopy %SOURCE_PC1% %BACKUP%\PC1 /E /LOG+:%LOG%

echo.
echo [3/3] Backing up PC2...
robocopy %SOURCE_PC2% %BACKUP%\PC2 /E /LOG+:%LOG%

echo.
echo ============================================
echo    BACKUP COMPLETE - %date% %time%
echo ============================================
pause