1. I provided JMeter load testing script below

<?xml version="1.0" encoding="UTF-8"?>
<jmeterTestPlan version="1.2" properties="5.0" jmeter="5.6.3">
  <hashTree>
    <TestPlan guiclass="TestPlanGui" testclass="TestPlan" testname="Test">
      <elementProp name="TestPlan.user_defined_variables" elementType="Arguments" guiclass="ArgumentsPanel" testclass="Arguments" testname="User Defined Variables">
        <collectionProp name="Arguments.arguments"/>
      </elementProp>
    </TestPlan>
    <hashTree>
      <ThreadGroup guiclass="ThreadGroupGui" testclass="ThreadGroup" testname="Thread Group">
        <intProp name="ThreadGroup.num_threads">200</intProp>
        <intProp name="ThreadGroup.ramp_time">30</intProp>
        <boolProp name="ThreadGroup.same_user_on_next_iteration">true</boolProp>
        <stringProp name="ThreadGroup.on_sample_error">continue</stringProp>
        <elementProp name="ThreadGroup.main_controller" elementType="LoopController" guiclass="LoopControlPanel" testclass="LoopController" testname="Loop Controller">
          <stringProp name="LoopController.loops">1</stringProp>
          <boolProp name="LoopController.continue_forever">false</boolProp>
        </elementProp>
      </ThreadGroup>
      <hashTree>
        <HTTPSamplerProxy guiclass="HttpTestSampleGui" testclass="HTTPSamplerProxy" testname="products">
          <stringProp name="HTTPSampler.domain">127.0.0.1</stringProp>
          <stringProp name="HTTPSampler.port">8001</stringProp>
          <stringProp name="HTTPSampler.protocol">http</stringProp>
          <stringProp name="HTTPSampler.path">/api/products/</stringProp>
          <boolProp name="HTTPSampler.follow_redirects">true</boolProp>
          <stringProp name="HTTPSampler.method">GET</stringProp>
          <boolProp name="HTTPSampler.use_keepalive">true</boolProp>
          <boolProp name="HTTPSampler.postBodyRaw">false</boolProp>
          <elementProp name="HTTPsampler.Arguments" elementType="Arguments" guiclass="HTTPArgumentsPanel" testclass="Arguments" testname="User Defined Variables">
            <collectionProp name="Arguments.arguments"/>
          </elementProp>
        </HTTPSamplerProxy>
        <hashTree/>
        <ResultCollector guiclass="ViewResultsFullVisualizer" testclass="ResultCollector" testname="View Results Tree">
          <boolProp name="ResultCollector.error_logging">false</boolProp>
          <objProp>
            <name>saveConfig</name>
            <value class="SampleSaveConfiguration">
              <time>true</time>
              <latency>true</latency>
              <timestamp>true</timestamp>
              <success>true</success>
              <label>true</label>
              <code>true</code>
              <message>true</message>
              <threadName>true</threadName>
              <dataType>true</dataType>
              <encoding>false</encoding>
              <assertions>true</assertions>
              <subresults>true</subresults>
              <responseData>false</responseData>
              <samplerData>false</samplerData>
              <xml>false</xml>
              <fieldNames>true</fieldNames>
              <responseHeaders>false</responseHeaders>
              <requestHeaders>false</requestHeaders>
              <responseDataOnError>false</responseDataOnError>
              <saveAssertionResultsFailureMessage>true</saveAssertionResultsFailureMessage>
              <assertionsResultsToSave>0</assertionsResultsToSave>
              <bytes>true</bytes>
              <sentBytes>true</sentBytes>
              <url>true</url>
              <threadCounts>true</threadCounts>
              <idleTime>true</idleTime>
              <connectTime>true</connectTime>
            </value>
          </objProp>
          <stringProp name="filename"></stringProp>
        </ResultCollector>
        <hashTree/>
        <ResultCollector guiclass="SummaryReport" testclass="ResultCollector" testname="Summary Report">
          <boolProp name="ResultCollector.error_logging">false</boolProp>
          <objProp>
            <name>saveConfig</name>
            <value class="SampleSaveConfiguration">
              <time>true</time>
              <latency>true</latency>
              <timestamp>true</timestamp>
              <success>true</success>
              <label>true</label>
              <code>true</code>
              <message>true</message>
              <threadName>true</threadName>
              <dataType>true</dataType>
              <encoding>false</encoding>
              <assertions>true</assertions>
              <subresults>true</subresults>
              <responseData>false</responseData>
              <samplerData>false</samplerData>
              <xml>false</xml>
              <fieldNames>true</fieldNames>
              <responseHeaders>false</responseHeaders>
              <requestHeaders>false</requestHeaders>
              <responseDataOnError>false</responseDataOnError>
              <saveAssertionResultsFailureMessage>true</saveAssertionResultsFailureMessage>
              <assertionsResultsToSave>0</assertionsResultsToSave>
              <bytes>true</bytes>
              <sentBytes>true</sentBytes>
              <url>true</url>
              <threadCounts>true</threadCounts>
              <idleTime>true</idleTime>
              <connectTime>true</connectTime>
            </value>
          </objProp>
          <stringProp name="filename"></stringProp>
        </ResultCollector>
        <hashTree/>
        <HTTPSamplerProxy guiclass="HttpTestSampleGui" testclass="HTTPSamplerProxy" testname="orders">
          <stringProp name="HTTPSampler.domain">127.0.0.1</stringProp>
          <stringProp name="HTTPSampler.port">8002</stringProp>
          <stringProp name="HTTPSampler.protocol">http</stringProp>
          <stringProp name="HTTPSampler.path">/api/orders</stringProp>
          <boolProp name="HTTPSampler.follow_redirects">true</boolProp>
          <stringProp name="HTTPSampler.method">GET</stringProp>
          <boolProp name="HTTPSampler.use_keepalive">true</boolProp>
          <boolProp name="HTTPSampler.postBodyRaw">false</boolProp>
          <elementProp name="HTTPsampler.Arguments" elementType="Arguments" guiclass="HTTPArgumentsPanel" testclass="Arguments" testname="User Defined Variables">
            <collectionProp name="Arguments.arguments"/>
          </elementProp>
        </HTTPSamplerProxy>
        <hashTree/>
      </hashTree>
    </hashTree>
  </hashTree>
</jmeterTestPlan>


2. And Performance Report

timeStamp,elapsed,label,responseCode,responseMessage,threadName,dataType,success,failureMessage,bytes,sentBytes,grpThreads,allThreads,URL,Latency,IdleTime,Connect
1734023396898,39,products,200,OK,Thread Group 1-1,text,true,,2940,129,1,1,http://127.0.0.1:8001/api/products/,39,0,1
1734023396938,35,orders,200,OK,Thread Group 1-1,text,true,,1246,253,1,1,http://127.0.0.1:8002/api/orders/,16,0,1
1734023396938,16,orders-0,301,Moved Permanently,Thread Group 1-1,text,true,,311,126,1,1,http://127.0.0.1:8002/api/orders,16,0,1
1734023396954,19,orders-1,200,OK,Thread Group 1-1,text,true,,935,127,1,1,http://127.0.0.1:8002/api/orders/,19,0,0
1734023397053,10,products,200,OK,Thread Group 1-2,text,true,,2942,129,1,1,http://127.0.0.1:8001/api/products/,10,0,0
1734023397063,34,orders,200,OK,Thread Group 1-2,text,true,,1248,253,1,1,http://127.0.0.1:8002/api/orders/,16,0,0
1734023397063,16,orders-0,301,Moved Permanently,Thread Group 1-2,text,true,,311,126,1,1,http://127.0.0.1:8002/api/orders,16,0,0
1734023397079,18,orders-1,200,OK,Thread Group 1-2,text,true,,937,127,1,1,http://127.0.0.1:8002/api/orders/,18,0,0
1734023397203,18,products,200,OK,Thread Group 1-3,text,true,,2943,129,1,1,http://127.0.0.1:8001/api/products/,18,0,0
1734023397222,47,orders,200,OK,Thread Group 1-3,text,true,,1250,253,1,1,http://127.0.0.1:8002/api/orders/,23,0,1
1734023397222,23,orders-0,301,Moved Permanently,Thread Group 1-3,text,true,,311,126,1,1,http://127.0.0.1:8002/api/orders,23,0,1
1734023397246,23,orders-1,200,OK,Thread Group 1-3,text,true,,939,127,1,1,http://127.0.0.1:8002/api/orders/,23,0,0
1734023397353,13,products,200,OK,Thread Group 1-4,text,true,,2940,129,1,1,http://127.0.0.1:8001/api/products/,12,0,1
1734023397366,38,orders,200,OK,Thread Group 1-4,text,true,,1250,253,1,1,http://127.0.0.1:8002/api/orders/,17,0,1
1734023397366,17,orders-0,301,Moved Permanently,Thread Group 1-4,text,true,,311,126,1,1,http://127.0.0.1:8002/api/orders,17,0,1
1734023397383,21,orders-1,200,OK,Thread Group 1-4,text,true,,939,127,1,1,http://127.0.0.1:8002/api/orders/,20,0,0
1734023397503,11,products,200,OK,Thread Group 1-5,text,true,,2941,129,1,1,http://127.0.0.1:8001/api/products/,11,0,0
1734023397514,38,orders,200,OK,Thread Group 1-5,text,true,,1251,253,1,1,http://127.0.0.1:8002/api/orders/,17,0,0
1734023397514,17,orders-0,301,Moved Permanently,Thread Group 1-5,text,true,,311,126,1,1,http://127.0.0.1:8002/api/orders,17,0,0
1734023397531,21,orders-1,200,OK,Thread Group 1-5,text,true,,940,127,1,1,http://127.0.0.1:8002/api/orders/,21,0,1
1734023397654,17,products,200,OK,Thread Group 1-6,text,true,,2941,129,1,1,http://127.0.0.1:8001/api/products/,16,0,0
1734023397672,44,orders,200,OK,Thread Group 1-6,text,true,,1251,253,1,1,http://127.0.0.1:8002/api/orders/,21,0,0
1734023397672,21,orders-0,301,Moved Permanently,Thread Group 1-6,text,true,,311,126,1,1,http://127.0.0.1:8002/api/orders,21,0,0
1734023397693,23,orders-1,200,OK,Thread Group 1-6,text,true,,940,127,1,1,http://127.0.0.1:8002/api/orders/,23,0,0
1734023397803,17,products,200,OK,Thread Group 1-7,text,true,,2941,129,1,1,http://127.0.0.1:8001/api/products/,17,0,1
1734023397821,44,orders,200,OK,Thread Group 1-7,text,true,,1249,253,1,1,http://127.0.0.1:8002/api/orders/,21,0,1
1734023397821,21,orders-0,301,Moved Permanently,Thread Group 1-7,text,true,,311,126,1,1,http://127.0.0.1:8002/api/orders,21,0,1
1734023397842,23,orders-1,200,OK,Thread Group 1-7,text,true,,938,127,1,1,http://127.0.0.1:8002/api/orders/,23,0,0
1734023397951,14,products,200,OK,Thread Group 1-8,text,true,,2942,129,1,1,http://127.0.0.1:8001/api/products/,14,0,1
1734023397966,39,orders,200,OK,Thread Group 1-8,text,true,,1250,253,1,1,http://127.0.0.1:8002/api/orders/,21,0,0
1734023397966,21,orders-0,301,Moved Permanently,Thread Group 1-8,text,true,,311,126,1,1,http://127.0.0.1:8002/api/orders,21,0,0
1734023397987,18,orders-1,200,OK,Thread Group 1-8,text,true,,939,127,1,1,http://127.0.0.1:8002/api/orders/,18,0,0
1734023398103,11,products,200,OK,Thread Group 1-9,text,true,,2941,129,1,1,http://127.0.0.1:8001/api/products/,11,0,0
1734023398115,39,orders,200,OK,Thread Group 1-9,text,true,,1248,253,1,1,http://127.0.0.1:8002/api/orders/,18,0,0
1734023398115,18,orders-0,301,Moved Permanently,Thread Group 1-9,text,true,,311,126,1,1,http://127.0.0.1:8002/api/orders,18,0,0
1734023398133,21,orders-1,200,OK,Thread Group 1-9,text,true,,937,127,1,1,http://127.0.0.1:8002/api/orders/,21,0,0
1734023398253,15,products,200,OK,Thread Group 1-10,text,true,,2940,129,1,1,http://127.0.0.1:8001/api/products/,15,0,0
1734023398269,41,orders,200,OK,Thread Group 1-10,text,true,,1249,253,1,1,http://127.0.0.1:8002/api/orders/,20,0,1
1734023398269,20,orders-0,301,Moved Permanently,Thread Group 1-10,text,true,,311,126,1,1,http://127.0.0.1:8002/api/orders,20,0,1
1734023398289,21,orders-1,200,OK,Thread Group 1-10,text,true,,938,127,1,1,http://127.0.0.1:8002/api/orders/,21,0,1
1734023398402,11,products,200,OK,Thread Group 1-11,text,true,,2941,129,1,1,http://127.0.0.1:8001/api/products/,11,0,0
1734023398414,40,orders,200,OK,Thread Group 1-11,text,true,,1250,253,1,1,http://127.0.0.1:8002/api/orders/,19,0,1
1734023398414,19,orders-0,301,Moved Permanently,Thread Group 1-11,text,true,,311,126,1,1,http://127.0.0.1:8002/api/orders,19,0,1
1734023398433,21,orders-1,200,OK,Thread Group 1-11,text,true,,939,127,1,1,http://127.0.0.1:8002/api/orders/,21,0,0
1734023398549,7,products,200,OK,Thread Group 1-12,text,true,,2943,129,1,1,http://127.0.0.1:8001/api/products/,7,0,1
1734023398557,26,orders,200,OK,Thread Group 1-12,text,true,,1248,253,1,1,http://127.0.0.1:8002/api/orders/,11,0,0
1734023398557,11,orders-0,301,Moved Permanently,Thread Group 1-12,text,true,,311,126,1,1,http://127.0.0.1:8002/api/orders,11,0,0
1734023398569,14,orders-1,200,OK,Thread Group 1-12,text,true,,937,127,1,1,http://127.0.0.1:8002/api/orders/,14,0,0
1734023398700,11,products,200,OK,Thread Group 1-13,text,true,,2943,129,1,1,http://127.0.0.1:8001/api/products/,11,0,0