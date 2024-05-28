function open_edition_modal(url) {
	$('#edition').load(url, function () {
		$(this).modal('show');
	});
}

function open_delete_modal(url) {
	$('#confirm_delete').load(url, function () {
		$(this).modal('show');
	});
}

function close_edition_modal() {
	$('#edicion').modal('hide');
}