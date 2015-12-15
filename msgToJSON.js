var myarray=new Array();
if(msg.payload.indexOf("HTTP_TRACE_REP")==0)
{
    var temp=msg.payload.split('#');
    var type=temp[0].slice(0,temp[0].indexOf('|'));
    myarray.push(type);
    if(type=="HTTP_TRACE_REP")
    {
        var userIP=temp[0].split('|')[3].split(':')[0];
        var hostIP=temp[0].split('|')[2].split(':')[0];
    }
    else
    {
        hostIP=temp[0].split('|')[3].split(':')[0];
        userIP=temp[0].split('|')[2].split(':')[0];
    }
    myarray.push(userIP);
    myarray.push(hostIP);
    var last=temp[1];
    var lastTemp=last.split('|');
    var taget=lastTemp[3];
    myarray.push(taget);
    var status=lastTemp[4];
    myarray.push(status);
    var hoststring=last.substring(last.indexOf("Host: ")+6,last.length);
    var host=hoststring.substring(0,hoststring.indexOf('\n'));
    myarray.push(host);
    var user_agentstring=last.substring(last.indexOf("User-Agent: ")+12,last.length);
    var user_agent=user_agentstring.substring(0,user_agentstring.indexOf('\n'));
    myarray.push(user_agent);
    var referer_string=last.substring(last.indexOf("Referer: ")+9,last.length);
    var referer=referer_string.substring(0,referer_string.indexOf('\n'));
    myarray.push(referer);
    msg.payload={
      "type":myarray[0],
      "userIP":myarray[1],
      "hostIP":myarray[2],
      "taget":myarray[3],
      "status":myarray[4],
      "host":myarray[5],
      "user-agent":myarray[6],
      "referer":myarray[7]
    };
    for(var i=0;i<myarray.length;i++)
    {
            myarray.pop();
    }
    return msg;
}

