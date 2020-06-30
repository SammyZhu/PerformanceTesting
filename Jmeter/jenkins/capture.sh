Jmeter_Home=/Applications/apache-jmeter-5.1.1/
$Jmeter_Home/bin/JMeterPluginsCMD.sh --generate-png $Jmeter_Home/report/png/RT_Time.png --input-jtl $Jmeter_Home/report/jtl/TestReport.jtl --plugin-type ResponseTimesOverTime
$Jmeter_Home/bin/JMeterPluginsCMD.sh --generate-png $Jmeter_Home/report/png/RT_Thread.png --input-jtl $Jmeter_Home/report/jtl/TestReport.jtl --plugin-type TimesVsThreads
$Jmeter_Home/bin/JMeterPluginsCMD.sh --generate-png $Jmeter_Home/report/png/TPS_Time.png --input-jtl $Jmeter_Home/report/jtl/TestReport.jtl --plugin-type TransactionsPerSecond
$Jmeter_Home/bin/JMeterPluginsCMD.sh --generate-png $Jmeter_Home/report/png/TPS_Thread.png --input-jtl $Jmeter_Home/report/jtl/TestReport.jtl --plugin-type ThroughputVsThreads
$Jmeter_Home/bin/JMeterPluginsCMD.sh --generate-png $Jmeter_Home/report/png/PerfMon.png --input-jtl $Jmeter_Home/report/jtl/perf.jtl --plugin-type PerfMon
