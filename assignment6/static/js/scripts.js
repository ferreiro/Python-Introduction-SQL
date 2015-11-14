// notesID 	= []; // All the ID's for notes of a user
readerWrapper = $('.reader-Wrapper'); // Modal box showed each time user click on a note.
reader = $('.reader');
previewClose = $('.reader-close');
 
previewClose.click(function() {
	hidePreviewNote();
});

$( ".Note-wrapper" ).each(function( index ) {

	// When clicked on "Note-link" open the Note in current window
	$(this).find('.Note-link').click(function(e) {
		
		note = $(this).parent();
		NoteID = note.attr('id');
		noteTitle = note.find('.Note-Title').html()
		noteContent = note.find('.Note-Content').html()
		noteInfo = "";

		url = 'api/notes/' + String(NoteID)
		$('#reader-loader').fadeIn('200');

		$.getJSON( url, function( data ) {
			if (data['valid'] == "false") {
				alert("Sorry... We couldn't retrieve information for that note... Try again");
			}
			else {
				changePreviewData(data); // Set note data on reader
				displayPreviewNote(); // Show the reader
				changeURL('#/' + data['Permalink']);
			}
		})
		.error(function() {
			alert("Sorry... We couldn't retrieve information for that note... Try later")
		})
		.complete(function() { 
			$('#reader-loader').fadeOut('200');
		});

		return false;
	});

});

function displayPreviewNote() {
	reader.delay('2000').addClass('reader-ZoomIn', 'slow', 'easeInOutElastic');
	readerWrapper.fadeIn('slow', 'easeInOutElastic');
}
function hidePreviewNote() {
	changeURL('');
	reader.delay('2000').removeClass('reader-ZoomIn', 'slow', 'easeInOutElastic');
	readerWrapper.fadeOut('slow', 'easeInOutElastic');
}
function changePreviewData(note) {
	// Use the box ide to get the text of title...
	$('.reader-Title').html(note['Title']);
	$('.reader-Content').html(note['Content']);
}

function getNoteInformation(NoteID) {
	note = undefined
	url = 'api/notes/' + String(NoteID)
	$('#reader-loader').fadeIn('200');


	$.getJSON( url, function( data ) {
		console.log(JSON.parse(data))
		//return JSON.parse(data);
		 //$.each( data, function( key, val ) {
	    //items.push( "<li id='" + key + "'>" + val + "</li>" );
	  });

	$.ajax({
	    type        : 'GET',       // define the type of HTTP verb we want to use (POST for our form)
	    url         : url, // the url where we want to POST
	    //data        : data,     // our data object
	    dataType    : 'json',       // what type of data do we expect back from the server
	    encode      : true
	})
	.done(function(response) {
		note = response;
		console.log(note)
	 })
	.fail(function(response) {
	    // si el server se ha hecho la picha un lio
	})
	.always(function(response) {
	   // Codigo para hacer siempre
	   $('#reader-loader').delay('100').fadeOut('100');
	});
	
	return note;
}

function changeURL (Permalink) {
	window.location = String(Permalink);
} 


