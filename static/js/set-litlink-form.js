
selector_clicked_func = function(){
            // Get id of the selected item
            var choice = $(this).children("option:selected").attr("id");
            $("#form-div").load('/form');
            console.log(choice + ' clicked')    
            
            $.ajax({
                url:"/form",
                type: 'POST',
                data: JSON.stringify({'selected_link': choice}),
                dataType: "json",
                contentType: 'application/json;charset=UTF-8',
                success: function() {        }
            }); 

}


// Main function
main = function(){
        // Selector handler
        $("#ll-selector").click(selector_clicked_func)
            
         
}

$(document).ready(main)
