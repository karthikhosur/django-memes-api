
// Start here
$("input[value*='MEASUREMENTS_Title4']").each(function () {
    $("<a name='expand_MEASUREMENTS_Title4' style='float:left ;'>       &#8197;&#8197; &#10148; &#8197;&#8197;      </a>").insertAfter($(this).parent());
    $(this).parent().next().on("click", function () {
        $("input[value*='MEASUREMENTS4.']").each(function () {
            if ($(this).is(":visible")) {
                $(this).parent().hide();
                $(this).hide();
            } else {
                $(this).parent().show();
                $(this).before("<p>   </p>");
                $(this).show();
            }

        })
    })
});

// End Here
// Start here
$("input[value*='DIAGNOSIS_']").each(function () {
    $("<a name='expand_DIAGNOSIS' style='float:left ;'>       &#8197;&#8197; &#10148; &#8197;&#8197;      </a>").insertAfter($(this).parent());
    $(this).parent().next().on("click", function () {
        $("input[value*='DIAGNOSIS.']").each(function () {
            if ($(this).is(":visible")) {
                $(this).parent().hide();
                $(this).hide();
            } else {
                $(this).parent().show();
                $(this).before("<p>   </p>");
                $(this).show();
            }

        })
    })
});

// End Here


// Start here
$("input[value*='PROCEDURES_']").each(function () {
    $("<a name='expand_PROCEDURES' style='float:left ;'>       &#8197;&#8197; &#10148; &#8197;&#8197;      </a>").insertAfter($(this).parent());
    $(this).parent().next().on("click", function () {
        $("input[value*='PROCEDURES.']").each(function () {
            if ($(this).is(":visible")) {
                $(this).parent().hide();
                $(this).hide();
            } else {
                $(this).parent().show();
                $(this).before("<p>   </p>");
                $(this).show();
            }

        })
    })
});

// End Here


// Start here
$("input[value*='MEDICATIONS_']").each(function () {
    $("<a name='expand_MEDICATIONS' style='float:left ;'>       &#8197;&#8197; &#10148; &#8197;&#8197;      </a>").insertAfter($(this).parent());
    $(this).parent().next().on("click", function () {
        $("input[value*='MEDICATIONS.']").each(function () {
            if ($(this).is(":visible")) {
                $(this).parent().hide();
                $(this).hide();
            } else {
                $(this).parent().show();
                $(this).before("<p>   </p>");
                $(this).show();
            }

        })
    })
});

// End Here
// Start here
$("input[value*='NOTES_']").each(function () {
    $("<a name='expand_NOTES' style='float:left ;'>       &#8197;&#8197; &#10148; &#8197;&#8197;      </a>").insertAfter($(this).parent());
    $(this).parent().next().on("click", function () {
        $("input[value*='NOTES.']").each(function () {
            if ($(this).is(":visible")) {
                $(this).parent().hide();
                $(this).hide();
            } else {
                $(this).parent().show();
                $(this).before("<p>   </p>");
                $(this).show();
            }

        })
    })
});

// End Here
// Start here
$("input[value*='EEG_']").each(function () {
    $("<a name='expand_EEG' style='float:left ;'>       &#8197;&#8197; &#10148; &#8197;&#8197;      </a>").insertAfter($(this).parent());
    $(this).parent().next().on("click", function () {
        $("input[value*='EEG.']").each(function () {
            if ($(this).is(":visible")) {
                $(this).parent().hide();
                $(this).hide();
            } else {
                $(this).parent().show();
                $(this).before("<p>   </p>");
                $(this).show();
            }

        })
    })
});

// End Here
// Start here
$("input[value*='IMAGING_']").each(function () {
    $("<a name='expand_IMAGING' style='float:left ;'>       &#8197;&#8197; &#10148; &#8197;&#8197;      </a>").insertAfter($(this).parent());
    $(this).parent().next().on("click", function () {
        $("input[value*='IMAGING.']").each(function () {
            if ($(this).is(":visible")) {
                $(this).parent().hide();
                $(this).hide();
            } else {
                $(this).parent().show();
                $(this).before("<p>   </p>");
                $(this).show();
            }

        })
    })
});

// End Here

// Start here
$("input[value*='Death_Data_']").each(function () {
    $("<a name='expand_Death_Data' style='float:left ;'>       &#8197;&#8197; &#10148; &#8197;&#8197;      </a>").insertAfter($(this).parent());
    $(this).parent().next().on("click", function () {
        $("input[value*='Death_Data.']").each(function () {
            if ($(this).is(":visible")) {
                $(this).parent().hide();
                $(this).hide();
            } else {
                $(this).parent().show();
                $(this).before("<p>   </p>");
                $(this).show();
            }

        })
    })
});

        // End Here

