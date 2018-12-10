tell application "Terminal"
	set currentTab to do script ("cd")
	delay 0.2
	do script ("cd Documents") in currentTab
	delay 0.2
	do script ("open J1.key") in currentTab
	delay 1.5
	quit
end tell

-- IF KEYNOTE IS ACTIVE AND NOT PLAYING THEN
-- GO TO THE FIRST SLIDE AND START IT
if running of application "Keynote" is true then
	tell application "Keynote"
		activate
		tell application "System Events"
			tell process "Keynote"
				click menu item "First Slide" of menu 1 of menu item "Go To" of menu 1 of menu bar item "Slide" of menu bar 1
				tell application "Keynote"
					try
						if playing is false then start the front document
					end try
				end tell
			end tell
		end tell
	end tell
end if
