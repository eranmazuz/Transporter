
$(document).ready(function(){
    $(".transporter_field").on('input', function(event) {
      var transporter_size = $(this).parent('td').find('.transporter_size').val();
      var occupied_seats = $(this).parent('td').find('.transporter_occupied_seats');
      occupied_seats.val($(this).val() * transporter_size).change();
   });

    $(".transporter_occupied_seats").on('change', function(event) {
        var remaining_soldiers = $(this).parents('tr').find('.soldier_count').val();

      var transporter_size = $(this).parents('tr').find('.transporter_occupied_seats').each(function () {
          remaining_soldiers = remaining_soldiers - $(this).val()
      });
      var occupied_seats = $(this).parents('tr').find('.soldiers_remainders').val(Math.max(0,remaining_soldiers));
   });

});
