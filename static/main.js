$(function() {

  $("#make_select").change(function() {
    var make_id = $("#make_select").val();
    var get_request = $.ajax({
      type: 'GET',
      url: '/' + make_id + '/',
    });

    get_request.done(function(data){
      console.log(data)
      var option_list = [["", "Select a model"]].concat(data);

      $("#model_select").empty();
        for (var i = 0; i < option_list.length; i++) {
          $("#model_select").append(
            $("<option></option>").attr("value", option_list[i][0]).text(option_list[i][1]));
        }
      $("#model_select").show();
    });
  });

  $("#submit-btn").click(function(e) {
    e.preventDefault()
    var make = $("#make_select").find(":selected").text();
    var model = $("#model_select").find(":selected").text();
    var make_id = $("#make_select").val();
    var model_id = $("#model_select").val();
    $("#chosen_make").html(make);
    $("#chosen_model").html(model);
    $("#selection").show();
    console.log("Make ID ", make_id)
    console.log("Model ID ", model_id)
  });

});