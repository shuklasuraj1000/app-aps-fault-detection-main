
var doc = new jsPDF();
    var specialElementHandlers = {
        '#editor': function (element, renderer) {
            return true;
        }
    };
    
  


    function Export() {
        html2canvas(document.getElementById('tblCustomers'), {
            onrendered: function (canvas) {
                var data = canvas.toDataURL();
                var docDefinition = {
                    content: [{
                        image: data,
                        width: 500
                    }]
                };
                pdfMake.createPdf(docDefinition).download("Table.pdf");
            }
        });
    }
   
    function search()
    {
        let input=document.getElementById("i").value;
    
        const pnumber = [
        "NAS1727", "ASNA2352", "ABS0997", "ABS0100","ABS0258","ABS0807","ASNA2352" ];
    
        const status = ["ACR + ACF", "ACR+ACF", "NO", "pe ACF","pe ACF","NO","ACF"];
    
        if(pnumber.includes(input)) {

         let i = pnumber.indexOf(input);
    
           document.getElementById("P_nubmer").innerHTML="<b> Part Number :- <b> "+pnumber[i];
    
           document.getElementById("status").innerHTML="<b> ACF_STATUS :- <b> "+status[i];
           document.getElementById("wstatus").innerHTML="";
         
        }else { 
            document.getElementById("P_nubmer").innerHTML="";
    
           document.getElementById("status").innerHTML="";   
           document.getElementById("wstatus").innerHTML="Enter Correct Data";
          //console.log("Not Found")
        }

        input = "";
    
    }
    
    
    
    