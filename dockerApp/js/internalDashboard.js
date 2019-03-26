$(document).ready(function() {
	function getErrorinPrediction(){
		$.ajax({
			url: "/checkLivePredictionQuality",
			type: "GET",
			success: function(returnData){
				if (returnData.response_code == 200) {
					$("#notice").empty();
					$("#notice").removeClass("alert alert-danger");
					$("#cmulighton").text("Light On Time: " + returnData.data.cmuMorningDateTime)
					$("#cmulightoff").text("Light Off Time: " + returnData.data.cmuEveningDateTime)

					$("#predAlighton").text("Predicted On Time: " + returnData.data.predictionMorningTimeA)
					$("#predAlightoff").text("Predicted Off Time: " + returnData.data.predictionEveningTimeA)

					$("#errorAlighton").text("Prediction Error: " + returnData.data.errorMorningA)
					$("#errorAlightoff").text("Prediction Error: " + returnData.data.errorEveningA)

					$("#mselighton").text("Light On Time: " + returnData.data.mseMorningDateTime)
					$("#mselightoff").text("Light Off Time: " + returnData.data.mseEveningDateTime)

					$("#predBlighton").text("Predicted On Time: " + returnData.data.predictionMorningTimeB)
					$("#predBlightoff").text("Predicted Off Time: " + returnData.data.predictionEveningTimeB)

					$("#errorBlighton").text("Prediction Error: " + returnData.data.errorMorningB)
					$("#errorBlightoff").text("Prediction Error: " + returnData.data.errorEveningB)


				} else {
					$("#notice").addClass("alert alert-danger")
					$("#notice").text(returnData.data)
				}

			},
			error: function(err){
				console.log(err);
			}
		});
	}
	setTimeout(function () {
		getErrorinPrediction();
	}, 3600)
});