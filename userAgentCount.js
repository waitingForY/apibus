var userIP=msg.payload.userIP;
var userAgent=msg.payload.userAgent;
msg.payload={
    "MsgID":"adminpush_tableuserAgentCount",
    "username":"admin",
    "payload":{
        "value":[
            ["userIP","userAgent"],
            [userIP,userAgent]
            ]
    }
};
msg.payload = JSON.stringify(msg.payload);
return msg;