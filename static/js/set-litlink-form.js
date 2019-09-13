
selector_clicked_func = function(){
            // Get id of the selected item
            var choice = $(this).children("option:selected").attr("id");

            console.log(choice + ' clicked')

            // send POST request with option id to flask and receive necessary div
            $.ajax({
                url:"/form_selector",
                type: 'POST',
                data: JSON.stringify({'selected_source': choice}),
                dataType: "json",
                contentType: 'application/json;charset=UTF-8',
                success: function(response) {
                    // Add form to the page
                    $("#form-div").empty();
                    $("#form-div").append(response);
                }});

};



submit_form_func = function(e){

            console.log('SUBMIT pressed');

            // get form id
            current_form = $("#submit_btn").parents('form:first').attr('id');
            console.log(current_form)

            // check if all inputs are not empty
            any_empty = false;
            $('input').each(function() {
            if(!$(this).val()){

                    // skip inputs which are allowed to be empty
                    if ($(this).hasClass('allow_empty')) {
                        return true;
                    }

                    // set red color to any empty input
                    $(this).css('border-color', 'red');
                    any_empty = true;
                }
            else {
                // set default color if input is not empty
                $(this).css('border-color', 'black');
            }
            });

            // don't submit form if any imput is empty
            if (any_empty == true){
                // clear the output area
                $("#output_area").empty();
                // exit this function
                return
            };


            // Create array of form inputs
            var form_data = $("#" + current_form).find(":input").filter(function () {
            return $.trim(this.value).length > 0
            }).serializeArray();

            // array ---> json
            var data_json = {};
            $(form_data).each(function(index, obj){
            data_json[obj.name] = obj.value;
            });

            // add form id to json
            data_json["form_name"] = current_form;

            console.log(data_json)

            // send data to backend
            $.ajax({
                type: "POST",
                url: "/form_handler",
                data: JSON.stringify(data_json),
                dataType: "json",
                contentType: 'application/json;charset=UTF-8',

                success: function(response) {

                    $("#output_area").empty();
                    $("#output_area").append(response);
                }



            })

}

// clear button
clear_textaria_func = function() {
    // clear output area
    $('#output_area').val('');
    $('input').each(function() {
        // clear input
        $(this).val('');
        // set black color
        $(this).css('border-color', 'black');
    });

    console.log('clear');

}

// copy button
copy_button_func = function() {
    $("#output_area").select();
    document.execCommand('copy');
}


// Main function
main = function(){
        // Selector handler
        $("#ll-selector").click(selector_clicked_func);
        $("#submit_btn").click(submit_form_func);
        $("#clear_btn").click(clear_textaria_func);
        $('#copy_btn').click(copy_button_func);
}

$(document).ready(main)


