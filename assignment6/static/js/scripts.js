// notesID 	= []; // All the ID's for notes of a user
previewNoteWrapper = $('.previewNote-Wrapper'); // Modal box showed each time user click on a note.
previewNote = $('.previewNote');
previewClose = $('.previewNote-close');
 
previewClose.click(function() {
	hidePreviewNote();
});

$( ".Note-wrapper" ).each(function( index ) {

	// When clicked on "Note-link" open the Note in current window
	$(this).find('.Note-link').click(function(e) {
		
		note = $(this).parent();
		noteID = $( this ).attr('id');
		noteTitle = note.find('.Note-Title').html()
		noteContent = note.find('.Note-Content').html()

		changePreviewData(noteTitle, noteContent); // Set note data on reader
		displayPreviewNote(); // Show the reader

		return false;
	});

});

function displayPreviewNote() {
	previewNote.delay('2000').addClass('previewNote-ZoomIn', 'slow', 'easeInOutElastic');
	previewNoteWrapper.fadeIn('slow', 'easeInOutElastic');
}
function hidePreviewNote() {
	previewNote.delay('2000').removeClass('previewNote-ZoomIn', 'slow', 'easeInOutElastic');
	previewNoteWrapper.fadeOut('slow', 'easeInOutElastic');
}
function changePreviewData(Title, Content) {
	// Use the box ide to get the text of title...
	$('.previewNote-Title').html(Title);
	$('.previewNote-Content').html(Content);
}


