$(function() {

  $("#make_select").change(function() {
    var make_id = $("#make_select").val();
    var get_request = $.ajax({
      type: 'GET',
      url: '/' + make_id + '/',
    });

    get_request.done(function(data){
      console.log(data)
      var option_list = data;

      $("#model_select").empty();
        for (var i = 0; i < option_list.length; i++) {
          $("#model_select").append(
            $("<option></option>").attr("value", option_list[i][0]).text(option_list[i][1]));
        }
    });
  });

  $("#submit-btn").click(function(e) {
    e.preventDefault()
    var make = $("#make_select").find(":selected").text();
    var model = $("#model_select").find(":selected").text();
    console.log(make, model)
  });

});