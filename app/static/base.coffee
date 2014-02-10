$ ->
    $("##{active_link}").addClass "active"

    $(".bxslider").bxSlider
        nextSelector: "#slider-next"
        prevSelector: "#slider-prev"
        nextText: "next"
        prevText: "prev"
