if(msg.payload.status=="304"||msg.payload.status=="500")
{
    msg.payload={"status":msg.payload.status,"errorPage":msg.payload.taget};
    return msg;
}
