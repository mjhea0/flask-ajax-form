$(function() {

  // test to ensure jQuery is working
  console.log("whee!")

  // disable refresh button
  $("#refresh-btn").prop("disabled", true)
  

  $("#make_select").change(function() {

    // grab value
    var make_id = $("#make_select").val();

    // send value via GET to URL /<make_id>
    var get_request = $.ajax({
      type: 'GET',
      url: '/' + make_id + '/',
    });

    // handle response
    get_request.done(function(data){

      // data
      console.log(data)

      // add values to list 
      var option_list = [["", "Select a model"]].concat(data);
      $("#model_select").empty();
        for (var i = 0; i < option_list.length; i++) {
          $("#model_select").append(
            $("<option></option>").attr("value", option_list[i][0]).text(option_list[i][1]));
        }
      // show model list
      $("#model_select").show();
    });
  });

  $("#submit-btn").click(function() {

    // grab values
    var make = $("#make_select").find(":selected").text();
    var model = $("#model_select").find(":selected").text();
    var make_id = $("#make_select").val();
    var model_id = $("#model_select").val();

    // append values to the DOM
    $("#chosen_make").html(make);
    $("#chosen_model").html(model);
    $("#chosen_make_id").html(make_id);
    $("#chosen_model_id").html(model_id);

    // show values selected
    $("#show_selection").show();
    // enable refresh button
    $("#refresh-btn").prop("disabled", false)
    // disable submit button
    $("#submit-btn").prop("disabled", true);

    // disable dropdown inputs
    $("#model_select").prop("disabled", true);
    $("#make_select").prop("disabled", true);
    $("#model_select").prop("disabled", true);
  });

  $("#refresh-btn").click(function() {

    // remove values to the DOM
    $("#chosen_make").html("");
    $("#chosen_model").html("");
    $("#chosen_make_id").html("");
    $("#chosen_model_id").html("");

    // hide values selected
    $("#show_selection").hide();
    // disable refresh button
    $("#refresh-btn").prop("disabled", true);
    // enable submit button
    $("#submit-btn").prop("disabled", false);
    // hide model list
    $("#model_select").hide();

    // enable dropdown inputs
    $("#model_select").prop("disabled", false);
    $("#make_select").prop("disabled", false);

   
  });

});