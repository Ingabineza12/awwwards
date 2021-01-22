// $(document).ready(function(){
//     $('form').submit(function(event){
//       event.preventDefault()
//     }) // End of submit event

//   }) // End of document ready function

  $(document).ready(function(){
    $('#fora').submit(function(event){
      event.preventDefault()
      form = $("#fora")

      $.ajax({
        'url':'/ajax/newsletter/',
        'type':'POST',
        'data':form.serialize(),
        'dataType':'json',
        'success': function(data){
          alert(data['success'])
        },
      })// END of Ajax method
      $('#id_your_name').val('')
      $("#id_email").val('')
    }) // End of submit event

  }) // End of document ready function
