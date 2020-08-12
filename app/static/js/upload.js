$(document).ready(function(){
	$('#drop').change(function(){
		
		var id = $('#folder').val();

		$.post("/drop",
		  {
		    folder: id
		  },
		  function(data, status){
			
			$('select').removeAttr('name');
			$('.selected').attr('name','folder');
		  	$('#drop').append(data)
		  	$('#folder').removeAttr('class');

		  	if($('.selected option').length  > 1) {
		  		$('#folder').removeAttr('id');
		  	} else {
		  	 	$('.selected').remove();
		  	}

		  });
	});
});