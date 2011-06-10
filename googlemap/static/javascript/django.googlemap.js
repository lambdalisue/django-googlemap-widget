/*
 * jQuery django-googlemapfield plugin
 * 
 * Author: 		giginet
 * Inspector:	alisue
 * 
 * Version: 0.1.0
 * 
 */
(function($){
	$.fn.googlemap = function(settings){
		// Set default arguments
		settings = jQuery.extend(true, {
			initial: {
				width:	"100%",
				height:	"320px"
			},
			query: {
				submit: {
					src:		"/static/image/django.googlemap.submit.png",
					alt:		"Submid address to a map",
					title:		"Submid address to a map"
				},
				loading: {
					src:		"/static/image/django.googlemap.loading.gif",
					alt:		"Loading..."
				},
				error: {
					src:		"/static/image/django.googlemap.error.png",
					alt:		"Failed to submit address to a map",
					title:		"Failed to submit address to a map"
				}
			},
			visibility: {
				show: {
					src:		"/static/image/django.googlemap.show.png",
					alt:		"Shwo a map",
					title:		"Show a map"
				},
				hide: {
					src:		"/static/image/django.googlemap.hide.png",
					alt:		"Hide a map",
					title:		"Hide a map"
				}
			},
			debug:	true
		}, settings);
		return $(this).each(function(){
			// Define global variables
			var $surface = $(this);
			var $latitude = $surface.attr('latitudeID') ? $("#" + $surface.attr('latitudeID')) : undefined;
			var $longitude = $surface.attr('longitudeID') ? $("#" + $surface.attr('longitudeID')) : undefined;
			var $zoom = $surface.attr('zoomID') ? $("#" + $surface.attr('zoomID')) : undefined;
			var $query = $surface.attr('queryID') ? $("#" + $surface.attr('queryID')) : undefined;
			var $show = $('<a>').attr({href: 'javascript:void(0);'});
			var $hide = $('<a>').attr({href: 'javascript:void(0);'});
			var gmap;
			var marker;
			var hidden = $surface.attr('hidden') ? true : false;
			var editable = $surface.attr('editable') ? true : false;
			// Related to Google Map
			function getInitialLocation(){
				var latitude = $surface.attr('latitude');
				var longitude = $surface.attr('longitude');
				var latlng = new google.maps.LatLng(latitude, longitude);
				return latlng;
			};
			function placeMarker(location){
				var latlng = undefined;
				if (location == undefined){
					latlng = getInitialLocation();
				}
				else{
					latlng = location;
				}
				marker.setPosition(latlng);
				$latitude.val(latlng.lat());
				$longitude.val(latlng.lng());
			};
			function createGoogleMap(){
				var latlng = getInitialLocation();
				var options = {
					zoom:		parseInt($surface.attr('zoom')),
					center:		latlng,
					mapTypeId:	google.maps.MapTypeId.ROADMAP
				};
				gmap = new google.maps.Map($surface.get(0), options);
				// Add Maker
				marker = new google.maps.Marker({
					clickable:	false,
					draggable:	editable,
					map:		gmap,
					position:	latlng
				});
				// Events
				if (editable) {
					google.maps.event.addListener(gmap, 'rightclick', function(event){
						placeMarker(event.latLng);
					});
					google.maps.event.addListener(gmap, 'zoom_changed', function(event){
						$zoom.val(gmap.getZoom());
					});
					google.maps.event.addListener(marker, 'dragend', function(event){
						placeMarker(event.latLng);
					});
				}
			};
				
			function addShowHideButtons(){
				$show.append($('<img style="vertical-align: middle">').attr({src: settings.visibility.show.src, alt: settings.visibility.show.alt, title: settings.visibility.show.title}));
				$hide.append($('<img style="vertical-align: middle">').attr({src: settings.visibility.hide.src, alt: settings.visibility.hide.alt, title: settings.visibility.hide.title}));
				$show.append(settings.visibility.show.alt);
				$hide.append(settings.visibility.hide.alt);
				$show = $('<p>').append($show);
				$hide = $('<p>').append($hide);
				// Append buttons
				$surface.after($show).after($hide);
				// Toggle
				if($surface.css('display') == 'none'){
					$show.show();
					$hide.hide();
				}else{
					$show.hide();
					$hide.show();
				}
				// Events
				$show.click(showSurface);
				$hide.click(hideSurface);
			};
			function showSurface(){
				$surface.fadeIn('fast', function(){
					google.maps.event.trigger(gmap, 'resize');
					gmap.setZoom(gmap.getZoom());
				});
				$show.hide('fast');
				$hide.show('fast');
				placeMarker();
			};
			function hideSurface(){
				$surface.fadeOut('fast');
				$show.show('fast');
				$hide.hide('fast');
				if ($longitude != undefined) {
					$longitude.val("");
				}
				if ($latitude != undefined) {
					$latitude.val("");
				}
			};
			function addGeocodeButton($query){
				if($query == undefined){
					return;
				}
				$query.css({'margin-right': '5px'});
				var $error = $('<img>').attr({src: settings.query.error.src, alt: settings.query.error.alt, title: settings.query.error.title});
				$error.css({display: 'none', 'vertical-align': 'middle'});
				var $loading = $('<img>').attr({src: settings.query.loading.src, alt: settings.query.loading.alt});
				$loading.css({display: 'none', 'vertical-align': 'middle'});
				var $submit = $('<a>').attr({href: 'javascript:void(0);'});
				$submit.css({'display': 'inline-block', 'vertical-align': 'middle', 'width': '16px', 'height': '16px', 'margin-right': '5px'});
				$submit.append($('<img>').attr({src: settings.query.submit.src, alt: settings.query.submit.alt, title: settings.query.submit.title}));
				// Append these elements after the $query
				$query.after($('<br />')).after('<small>Press TAB to submit address to a map</small>').after($error).after($loading).after($submit);
				// Create Geocoder
				var geocoder = new google.maps.Geocoder();
				function geocode(){
					var query = $query.val();
					$loading.show();
					$submit.hide();
					geocoder.geocode({'address': query}, function(results, status){
						$loading.hide();
						$submit.show();
						if (status == google.maps.GeocoderStatus.OK) {
							showSurface();
							var latlng = results[0].geometry.location;
							if (editable) {
								placeMarker(latlng);
							}
							gmap.setCenter(latlng);
							$error.hide();
						}else{
							$error.show();
						}
					});
				};
				$submit.click(geocode);
				$query.keydown(function(e){
					if (e.keyCode == 9) {
						geocode();
						return false;
					}
				});
			}
			// Modify surface size
			if ($surface.width() == 0) {
				$surface.css('width', settings.initial.width);
			}
			if ($surface.height() == 0){
				$surface.css('height', settings.initial.height);
			}
			createGoogleMap();
			
			// Create Show/Hide buttons
			addShowHideButtons();
			if (editable) {
				// Create Geocode button
				addGeocodeButton($query);
			}
			if(hidden){
				hideSurface();
			}
		});
	};
})(jQuery);
