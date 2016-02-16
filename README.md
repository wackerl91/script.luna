![alt tag](https://raw.github.com/wackerl91/luna/master/icon.png)

Luna aims to be a one-size-fits-all Moonlight launcher for Kodi. Even though it's tailored for OSMC right now, it can be easily extended to support pretty much any platform where both Kodi and Moonlight (embedded or PC) are available. Probably OSX will be next, but let me know which platforms you'd like to see supported! If you feel like a specific feature is missing don't hesitate to tell me and I'll see what I can do ;) 

Screenshots can be found on the [Wiki](https://github.com/wackerl91/luna/wiki)

## Prerequisites
[Moonlight-Embedded](https://github.com/irtimmer/moonlight-embedded) needs to be installed. For setup instructions please follow irtimmer's wiki.

## Installation
- Download from [release page](https://github.com/wackerl91/luna/releases)
- Copy to your OSMC installation or use a network share
- In Kodi: Settings > Addons > Install from zip file
- Before first starting the addon, you must enter at least the IP of the GameStream host in the addon settings. 

## Features
- GameStream Host Pairing can be done from within Luna
- Controller Mapping can be done there too (that's somewhat buggy though, at times I need to restart xboxdrv on my Pi before it works. Not sure if this is Luna or Moonlight ...)
- Dynamic Game Library
- the above allows for starting of specific games
- extensive configuration which supports nearly all of moonlight-embedded's launch options
- Game View similar to Kodi's movie view (cover art / fanart support)

## Issues
- Controller Mapping sometimes not working
- Please keep in mind that Luna - while I guess it's working pretty good right now - is still alpha, so don't expect it to work perfectly

## Credits
- Logo and Fanart by [Ben Biedrawa](http://sooulart.com)
- Icons made by [Freepik](http://www.flaticon.com/authors/freepik) from www.flaticon.com
- Game information and posters are provided by [OMDB](http://www.omdbapi.com) under CC-BY4.0
- Additional game information and posters provided by [TheGamesDB](http://thegamesdb.net)
- Some more information is being pulled from [IGDB](https://www.igdb.com) (very developer friendly terms, thank you so much!)
- Steam Background from DiglidiDudeNG over at [deviantart](http://diglididudeng.deviantart.com/art/Steam-Wallpaper-Globe-458081397)

## Bugs / Feature Requests
- Please report any bugs or feature requests on the issue tracker - I can only make Luna better if you're willing to report every issue you run into!
- If you're running into _any_ issue while using the scraper feature, please post the logs on the issue tracker or send me a PN on [OSMC forums](https://discourse.osmc.tv), my username is exxe (you may redact them if you don't want to post what games you're playing). They might be stupid bugs, but they're still there.
- Should you also run into issues using the controller mapping feature (i.e. not taking any input) please let me know in the issue tracker or via OSMC forum (see above) which controller / driver you're using
