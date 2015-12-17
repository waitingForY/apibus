if(msg.payload.status.indexOf("3")==0||msg.payload.status.indexOf("4")==0||msg.payload.status.indexOf("5")==0)
{
    var errType=msg.payload.status;
    var errURL=msg.payload.taget;
    msg.payload={
        "MsgID":"adminpush_tableerroCount",
        "username":"admin",
        "payload":{
            "value":[
                ["erroType","erroURL"],
                [errType,errURL]
        ]
        }
    };
    msg.payload = JSON.stringify(msg.payload);
    return msg;
}