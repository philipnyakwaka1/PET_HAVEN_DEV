// $(document).ready(function () {
//   // Initially, hide all products
//   $(".single-product-item").hide();

//   // Click event for filtering
//   $(".product-filters li").on("click", function () {
//     $(".product-filters li").removeClass("active");
//     $(this).addClass("active");

//     var filter = $(this).attr("data-filter");

//     // Hide all products
//     $(".single-product-item").hide();

//     // Show products based on filter
//     if (filter === "*") {
//       $(".single-product-item").show();
//     } else {
//       $(filter).closest(".col-md-6").show();
//     }
//   });
// });

// $(document).ready(function () {
//   // Initially, hide all products
//   $(".single-product-item").hide();

//   // Click event for filtering
//   $(".product-filters li").on("click", function () {
//     $(".product-filters li").removeClass("active");
//     $(this).addClass("active");

//     var filter = $(this).attr("data-filter");

//     // Hide all products
//     $(".single-product-item").hide();

//     // Show products based on filter
//     // if (filter === "*") {
//     //   $(".single-product-item").show();
//     // } else {
//     //   $(".single-product-item").each(function () {
//     //     if ($(this).hasClass(filter)) {
//     //       $(this).show();
//     //     }
//     //   });
//     // }
//     if (filter === "*") {
//       $(".product-lists .single-product-item").show();
//     } else {
//       $(".product-lists .single-product-item")
//         .filter("." + filterValue)
//         .show();
//     }
//   });
// });

// $(document).ready(function () {
//   $(".product-filters ul li").click(function () {
//     // Get the category filter value
//     var filterValue = $(this).attr("data-filter");

//     // Hide all products
//     $(".product-lists .single-product-item").hide();

//     // Show products belonging to the selected category
//     if (filterValue === "*") {
//       $(".product-lists .single-product-item").show();
//     } else {
//       $(".product-lists .single-product-item")
//         .filter("." + filterValue)
//         .show();
//     }

//     // Add 'active' class to the clicked filter and remove from others
//     $(this).addClass("active").siblings().removeClass("active");
//   });
// });

// $(document).ready(function () {
//   // Click event for filtering
//   $(".product-filters li").on("click", function () {
//     // Remove 'active' class from all filter options and add it to the clicked one
//     $(".product-filters li").removeClass("active");
//     $(this).addClass("active");

//     // Get the filter value
//     var filter = $(this).attr("data-filter");

//     // Hide all products
//     $(".single-product-item").hide();

//     // Show products based on filter
//     if (filter === "*") {
//       $(".single-product-item").show();
//     } else {
//       $(".single-product-item")
//         .filter("." + filter)
//         .show();
//     }
//   });
// });

// $(document).ready(function () {
//   // Click event for filtering
//   $(".product-filters li").on("click", function () {
//     // Remove 'active' class from all filter options and add it to the clicked one
//     $(".product-filters li").removeClass("active");
//     $(this).addClass("active");

//     // Get the filter value
//     var filter = $(this).attr("data-filter");

//     // Hide all products
//     $(".single-product-item").hide();

//     // Show products based on filter
//     if (filter === "*") {
//       $(".single-product-item").show();
//     } else {
//       $(".single-product-item").each(function () {
//         if ($(this).hasClass(filter)) {
//           $(this).show();
//         }
//       });
//     }
//   });
// });

// $(document).ready(function () {
//   // Click event for filtering
//   $(".product-filters li").on("click", function () {
//     // Remove 'active' class from all filter options and add it to the clicked one
//     $(".product-filters li").removeClass("active");
//     $(this).addClass("active");

//     // Get the filter value
//     var filter = $(this).attr("data-filter");

//     // Hide all products
//     $(".single-product-item").hide();

//     // Show products based on filter
//     if (filter === "*") {
//       $(".single-product-item").show();
//     } else {
//       $(".product-lists .single-product-item").hide();
//       $(".product-lists .single-product-item" + filter).show();
//     }
//   });
// });

// $(document).ready(function () {
//   // Click event for filtering
//   $(".product-filters li").on("click", function () {
//     // Remove 'active' class from all filter options and add it to the clicked one
//     $(".product-filters li").removeClass("active");
//     $(this).addClass("active");

//     // Get the filter value
//     var filter = $(this).attr("data-filter");

//     // Hide all products
//     $(".single-product-item").hide();

//     // Show products based on filter
//     if (filter === "*") {
//       $(".single-product-item").show();
//     } else {
//       $(".single-product-item" + filter).show();
//     }
//   });
// });

// $(document).ready(function () {
//   $(".product-filters li").on("click", function () {
//     $(".product-filters li").removeClass("active");
//     $(this).addClass("active");
//     var filter = $(this).attr("data-filter");
//     $(".single-product-item").hide();
//     if (filter === "*") {
//       $(".product-lists .single-product-item").show();
//     } else {
//       $(".product-lists .single-product-item").each(function () {
//         if ($(this).hasClass(filter)) {
//           $(this).show();
//         }
//       });
//     }
//   });
// });

// $(document).ready(function () {
//   $(".product-filters li").on("click", function () {
//     $(".product-filters li").removeClass("active");
//     $(this).addClass("active");
//     var filter = $(this).attr("data-filter");
//     $(".single-product-item").hide();
//     if (filter === "*") {
//       $(".product-lists .single-product-item").show();
//     } else {
//       $(".product-lists .single-product-item").hide();
//       $(".product-lists ." + filter).show();
//     }
//   });
// });

// $(document).ready(function () {
//   $(".product-filters li").on("click", function () {
//     $(".product-filters li").removeClass("active");
//     $(this).addClass("active");
//     var filter = $(this).attr("data-filter");
//     $(".single-product-item").hide();
//     if (filter === "*") {
//       $(".product-lists .single-product-item").show();
//     } else {
//       $(".product-lists ." + filter).show();
//     }
//   });
// });

$(document).ready(function () {
  $(".product-filters li").on("click", function () {
    $(".product-filters li").removeClass("active");
    $(this).addClass("active");
    var filter = $(this).attr("data-filter");
    $(".single-product-item").hide();
    if (filter === "*") {
      $(".product-lists .single-product-item").show();
    } else {
      $(".product-lists")
        .find("." + filter)
        .show()
        .addClass("filtered");
    }
  });
});
