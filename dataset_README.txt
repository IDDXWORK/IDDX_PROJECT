
The dataset contains front and rear view combined videos of dimension: 1920 pixel-width x 2160 pixel-height.

Each view has 1920 pixel-width and 1080 pixel-height. The pixel-height from 0 to 1079 corresponds to the frontview, while that from 1080 to 2159 corresponds to the rearview.

Each video is of one minute duration with 1500 frames (captured at 25 FPS).


Dataset directoy structure:

IDDX/
	|
	----iddx_videos/
	|	|
	|	--- <date-timestamp>*_0060_combined.mp4
	|
	----iddx_annotations.json

	
The "iddx_annotations.json" file contains the entire IDDX dataset labels. It comprises a list of driving scenarios or events with the following details:
[
	{
		event_id: (driving event's unique id)
		
		video_name: (video that contains the event)

		start_frame: (the event's start frame index in the video)
		
		end_frame: (the event's end frame index in the video)
		
		ego-vehicle_driving_behavior: (ego-vehicle's driving behavior when the event occured)
		
		data: (event corresponding to train/test/val data splits)
		
		IOs: (list of Important Objects (IOs) observed during the driving event)
			[
				{
					IO_id: 
					IO_track_and_frameno: (the IO track's bounding boxes in (x_min, y_min, x_max, y_max) format and the video-frame number at which the IO track's bounding box was annotated)
					[
						[x_min, y_min, x_max, y_max, video_frame_number],
						...
						...
					]
					IO_category: (type of IO, e.g. car, bus, motorcycle, etc.)

					IO_explanation: (explanation for the IO, e.g. Overtaking, Congestion, Confrontation, etc.)
					
					is_causal: (is it the primary IO influencing the ego-vehicle's behavior)
				}
			]


	},
	...
	...
]

Please visit IDD-X project webpage for additional details: https://idd-x.github.io/
