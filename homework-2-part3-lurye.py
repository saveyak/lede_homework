#Sharon Lurye
#6/12/21
#Homework 2, Part 3

import json
from typing import Counter

data = json.loads("{\"tracks\":[{\"album\":{\"album_type\":\"single\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/1YxmW7DO2dM05gwMKTbr7l\"},\"href\":\"https://api.spotify.com/v1/albums/1YxmW7DO2dM05gwMKTbr7l\",\"id\":\"1YxmW7DO2dM05gwMKTbr7l\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/5b14b24dea78b0a14244ccb86f3bfd20bf77326d\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/177939e6656bd0ae46d12e1f36e9162016d28a3c\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/7b42b976267520f4dbb2f67e1baa63ca13bdbfdb\",\"width\":64}],\"name\":\"Fake Love\",\"type\":\"album\",\"uri\":\"spotify:album:1YxmW7DO2dM05gwMKTbr7l\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":207813,\"explicit\":true,\"external_ids\":{\"isrc\":\"USCM51600333\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/6NMNgWgEAzde5M8U3lc6FN\"},\"href\":\"https://api.spotify.com/v1/tracks/6NMNgWgEAzde5M8U3lc6FN\",\"id\":\"6NMNgWgEAzde5M8U3lc6FN\",\"name\":\"Fake Love\",\"popularity\":90,\"preview_url\":\"https://p.scdn.co/mp3-preview/b1c79b52128cc45a962cb87ba5a616ea6a435356?cid=null\",\"track_number\":1,\"type\":\"track\",\"uri\":\"spotify:track:6NMNgWgEAzde5M8U3lc6FN\"},{\"album\":{\"album_type\":\"album\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/0G1ffjfFuTUTVjDrVdLimH\"},\"href\":\"https://api.spotify.com/v1/albums/0G1ffjfFuTUTVjDrVdLimH\",\"id\":\"0G1ffjfFuTUTVjDrVdLimH\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/e73c706e842eb5233eab7afd3404218a2696d568\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/90f080afbec29a0c58509875a6dd59b3c380e353\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/260c2e74e67a15cf61ac72f8264cc6caec5f7a66\",\"width\":64}],\"name\":\"Views\",\"type\":\"album\",\"uri\":\"spotify:album:0G1ffjfFuTUTVjDrVdLimH\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3tVQdUvClmAT7URs9V3rsp\"},\"href\":\"https://api.spotify.com/v1/artists/3tVQdUvClmAT7URs9V3rsp\",\"id\":\"3tVQdUvClmAT7URs9V3rsp\",\"name\":\"WizKid\",\"type\":\"artist\",\"uri\":\"spotify:artist:3tVQdUvClmAT7URs9V3rsp\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/77DAFfvm3O9zT5dIoG0eIO\"},\"href\":\"https://api.spotify.com/v1/artists/77DAFfvm3O9zT5dIoG0eIO\",\"id\":\"77DAFfvm3O9zT5dIoG0eIO\",\"name\":\"Kyla\",\"type\":\"artist\",\"uri\":\"spotify:artist:77DAFfvm3O9zT5dIoG0eIO\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":173986,\"explicit\":false,\"external_ids\":{\"isrc\":\"USCM51600028\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/12VWzyPDBCc8fqeWCAfNwR\"},\"href\":\"https://api.spotify.com/v1/tracks/12VWzyPDBCc8fqeWCAfNwR\",\"id\":\"12VWzyPDBCc8fqeWCAfNwR\",\"name\":\"One Dance\",\"popularity\":84,\"preview_url\":\"https://p.scdn.co/mp3-preview/98f60b086bb1da2ca2e4c217331b8c8cc801358d?cid=null\",\"track_number\":12,\"type\":\"track\",\"uri\":\"spotify:track:12VWzyPDBCc8fqeWCAfNwR\"},{\"album\":{\"album_type\":\"single\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/2z3NlPY0n0gHJPCPqrzA6V\"},\"href\":\"https://api.spotify.com/v1/albums/2z3NlPY0n0gHJPCPqrzA6V\",\"id\":\"2z3NlPY0n0gHJPCPqrzA6V\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/5b14b24dea78b0a14244ccb86f3bfd20bf77326d\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/177939e6656bd0ae46d12e1f36e9162016d28a3c\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/7b42b976267520f4dbb2f67e1baa63ca13bdbfdb\",\"width\":64}],\"name\":\"Sneakin’\",\"type\":\"album\",\"uri\":\"spotify:album:2z3NlPY0n0gHJPCPqrzA6V\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/1URnnhqYAYcrqrcwql10ft\"},\"href\":\"https://api.spotify.com/v1/artists/1URnnhqYAYcrqrcwql10ft\",\"id\":\"1URnnhqYAYcrqrcwql10ft\",\"name\":\"21 Savage\",\"type\":\"artist\",\"uri\":\"spotify:artist:1URnnhqYAYcrqrcwql10ft\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":251333,\"explicit\":true,\"external_ids\":{\"isrc\":\"USCM51600337\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/4ckuS4Nj4FZ7i3Def3Br8W\"},\"href\":\"https://api.spotify.com/v1/tracks/4ckuS4Nj4FZ7i3Def3Br8W\",\"id\":\"4ckuS4Nj4FZ7i3Def3Br8W\",\"name\":\"Sneakin’\",\"popularity\":82,\"preview_url\":\"https://p.scdn.co/mp3-preview/4fa89ace286252c33a1ca0d36e7555d6a451a2db?cid=null\",\"track_number\":1,\"type\":\"track\",\"uri\":\"spotify:track:4ckuS4Nj4FZ7i3Def3Br8W\"},{\"album\":{\"album_type\":\"album\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/0G1ffjfFuTUTVjDrVdLimH\"},\"href\":\"https://api.spotify.com/v1/albums/0G1ffjfFuTUTVjDrVdLimH\",\"id\":\"0G1ffjfFuTUTVjDrVdLimH\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/e73c706e842eb5233eab7afd3404218a2696d568\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/90f080afbec29a0c58509875a6dd59b3c380e353\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/260c2e74e67a15cf61ac72f8264cc6caec5f7a66\",\"width\":64}],\"name\":\"Views\",\"type\":\"album\",\"uri\":\"spotify:album:0G1ffjfFuTUTVjDrVdLimH\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/5pKCCKE2ajJHZ9KAiaK11H\"},\"href\":\"https://api.spotify.com/v1/artists/5pKCCKE2ajJHZ9KAiaK11H\",\"id\":\"5pKCCKE2ajJHZ9KAiaK11H\",\"name\":\"Rihanna\",\"type\":\"artist\",\"uri\":\"spotify:artist:5pKCCKE2ajJHZ9KAiaK11H\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":263373,\"explicit\":true,\"external_ids\":{\"isrc\":\"USCM51600088\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/7fJtPlEZKxu6gvkfBFc5tW\"},\"href\":\"https://api.spotify.com/v1/tracks/7fJtPlEZKxu6gvkfBFc5tW\",\"id\":\"7fJtPlEZKxu6gvkfBFc5tW\",\"name\":\"Too Good\",\"popularity\":79,\"preview_url\":\"https://p.scdn.co/mp3-preview/e702c76de627c3fb04da1bcbf6a8b53c3326a0cc?cid=null\",\"track_number\":16,\"type\":\"track\",\"uri\":\"spotify:track:7fJtPlEZKxu6gvkfBFc5tW\"},{\"album\":{\"album_type\":\"album\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/0G1ffjfFuTUTVjDrVdLimH\"},\"href\":\"https://api.spotify.com/v1/albums/0G1ffjfFuTUTVjDrVdLimH\",\"id\":\"0G1ffjfFuTUTVjDrVdLimH\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/e73c706e842eb5233eab7afd3404218a2696d568\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/90f080afbec29a0c58509875a6dd59b3c380e353\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/260c2e74e67a15cf61ac72f8264cc6caec5f7a66\",\"width\":64}],\"name\":\"Views\",\"type\":\"album\",\"uri\":\"spotify:album:0G1ffjfFuTUTVjDrVdLimH\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":245226,\"explicit\":true,\"external_ids\":{\"isrc\":\"USCM51600080\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/4CpKEkdGbOJV51cSvx7SoG\"},\"href\":\"https://api.spotify.com/v1/tracks/4CpKEkdGbOJV51cSvx7SoG\",\"id\":\"4CpKEkdGbOJV51cSvx7SoG\",\"name\":\"Controlla\",\"popularity\":79,\"preview_url\":\"https://p.scdn.co/mp3-preview/c5b5845dc83410f5731e395c5a725d6b6e94ff69?cid=null\",\"track_number\":11,\"type\":\"track\",\"uri\":\"spotify:track:4CpKEkdGbOJV51cSvx7SoG\"},{\"album\":{\"album_type\":\"album\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3ubFn9991d8ygM3MSi7NDi\"},\"href\":\"https://api.spotify.com/v1/artists/3ubFn9991d8ygM3MSi7NDi\",\"id\":\"3ubFn9991d8ygM3MSi7NDi\",\"name\":\"Future\",\"type\":\"artist\",\"uri\":\"spotify:artist:3ubFn9991d8ygM3MSi7NDi\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/1ozpmkWcCHwsQ4QTnxOOdT\"},\"href\":\"https://api.spotify.com/v1/albums/1ozpmkWcCHwsQ4QTnxOOdT\",\"id\":\"1ozpmkWcCHwsQ4QTnxOOdT\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/77b0c91524867cc72d1974f66ad8cd21d063a20e\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/f2405b82d0578dd815a3082ca0f7ec4e18e937a1\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/a5435bb3ab4fabe43bc7f7ce46a6c23aa30d8eae\",\"width\":64}],\"name\":\"What A Time To Be Alive\",\"type\":\"album\",\"uri\":\"spotify:album:1ozpmkWcCHwsQ4QTnxOOdT\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"},{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3ubFn9991d8ygM3MSi7NDi\"},\"href\":\"https://api.spotify.com/v1/artists/3ubFn9991d8ygM3MSi7NDi\",\"id\":\"3ubFn9991d8ygM3MSi7NDi\",\"name\":\"Future\",\"type\":\"artist\",\"uri\":\"spotify:artist:3ubFn9991d8ygM3MSi7NDi\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":205879,\"explicit\":true,\"external_ids\":{\"isrc\":\"USCM51500300\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/27GmP9AWRs744SzKcpJsTZ\"},\"href\":\"https://api.spotify.com/v1/tracks/27GmP9AWRs744SzKcpJsTZ\",\"id\":\"27GmP9AWRs744SzKcpJsTZ\",\"name\":\"Jumpman\",\"popularity\":77,\"preview_url\":\"https://p.scdn.co/mp3-preview/4f3e954bb232a96c196389017d961016c8cbd7fc?cid=null\",\"track_number\":9,\"type\":\"track\",\"uri\":\"spotify:track:27GmP9AWRs744SzKcpJsTZ\"},{\"album\":{\"album_type\":\"album\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/0G1ffjfFuTUTVjDrVdLimH\"},\"href\":\"https://api.spotify.com/v1/albums/0G1ffjfFuTUTVjDrVdLimH\",\"id\":\"0G1ffjfFuTUTVjDrVdLimH\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/e73c706e842eb5233eab7afd3404218a2696d568\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/90f080afbec29a0c58509875a6dd59b3c380e353\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/260c2e74e67a15cf61ac72f8264cc6caec5f7a66\",\"width\":64}],\"name\":\"Views\",\"type\":\"album\",\"uri\":\"spotify:album:0G1ffjfFuTUTVjDrVdLimH\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":267066,\"explicit\":false,\"external_ids\":{\"isrc\":\"USCM51500238\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/1OAYKfE0YdrN7C1yLWaLJo\"},\"href\":\"https://api.spotify.com/v1/tracks/1OAYKfE0YdrN7C1yLWaLJo\",\"id\":\"1OAYKfE0YdrN7C1yLWaLJo\",\"name\":\"Hotline Bling\",\"popularity\":75,\"preview_url\":\"https://p.scdn.co/mp3-preview/53a8f039eb0b567e47868f5a53de4683ba5d5f0c?cid=null\",\"track_number\":20,\"type\":\"track\",\"uri\":\"spotify:track:1OAYKfE0YdrN7C1yLWaLJo\"},{\"album\":{\"album_type\":\"album\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/0G1ffjfFuTUTVjDrVdLimH\"},\"href\":\"https://api.spotify.com/v1/albums/0G1ffjfFuTUTVjDrVdLimH\",\"id\":\"0G1ffjfFuTUTVjDrVdLimH\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/e73c706e842eb5233eab7afd3404218a2696d568\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/90f080afbec29a0c58509875a6dd59b3c380e353\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/260c2e74e67a15cf61ac72f8264cc6caec5f7a66\",\"width\":64}],\"name\":\"Views\",\"type\":\"album\",\"uri\":\"spotify:album:0G1ffjfFuTUTVjDrVdLimH\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":189853,\"explicit\":true,\"external_ids\":{\"isrc\":\"USCM51600078\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/4YJmZfvlheSziXem8HBWrj\"},\"href\":\"https://api.spotify.com/v1/tracks/4YJmZfvlheSziXem8HBWrj\",\"id\":\"4YJmZfvlheSziXem8HBWrj\",\"name\":\"Still Here\",\"popularity\":73,\"preview_url\":\"https://p.scdn.co/mp3-preview/39384d3485d21184dd3719cfd8d644182b0b1d8b?cid=null\",\"track_number\":10,\"type\":\"track\",\"uri\":\"spotify:track:4YJmZfvlheSziXem8HBWrj\"},{\"album\":{\"album_type\":\"single\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/79qV4McLzhs8U3FyRKnocz\"},\"href\":\"https://api.spotify.com/v1/albums/79qV4McLzhs8U3FyRKnocz\",\"id\":\"79qV4McLzhs8U3FyRKnocz\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/2151a609fd5a5ec69586920a85bf308cdf56f3a1\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/9c6eb30ff5270c115b1ecd2b74430e505c281f25\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/ef4e90b4dde72134365a732659dccf9e1bd7b519\",\"width\":64}],\"name\":\"Back To Back\",\"type\":\"album\",\"uri\":\"spotify:album:79qV4McLzhs8U3FyRKnocz\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":170637,\"explicit\":true,\"external_ids\":{\"isrc\":\"USCM51500241\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/5lFDtgWsjRJu8fPOAyJIAK\"},\"href\":\"https://api.spotify.com/v1/tracks/5lFDtgWsjRJu8fPOAyJIAK\",\"id\":\"5lFDtgWsjRJu8fPOAyJIAK\",\"name\":\"Back To Back\",\"popularity\":73,\"preview_url\":\"https://p.scdn.co/mp3-preview/b5bb11586af5cfde7c0eaef26300b2f6f62d2ac4?cid=null\",\"track_number\":1,\"type\":\"track\",\"uri\":\"spotify:track:5lFDtgWsjRJu8fPOAyJIAK\"},{\"album\":{\"album_type\":\"album\",\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"external_urls\":{\"spotify\":\"https://open.spotify.com/album/0ptlfJfwGTy0Yvrk14JK1I\"},\"href\":\"https://api.spotify.com/v1/albums/0ptlfJfwGTy0Yvrk14JK1I\",\"id\":\"0ptlfJfwGTy0Yvrk14JK1I\",\"images\":[{\"height\":640,\"url\":\"https://i.scdn.co/image/d329671363eb7826b5871eef978841c7db97c757\",\"width\":640},{\"height\":300,\"url\":\"https://i.scdn.co/image/bcd6801c26cb293a45df9b092227395c5b403b4c\",\"width\":300},{\"height\":64,\"url\":\"https://i.scdn.co/image/14d65d4565838431345e35575b8b74d95134990a\",\"width\":64}],\"name\":\"If You're Reading This It's Too Late\",\"type\":\"album\",\"uri\":\"spotify:album:0ptlfJfwGTy0Yvrk14JK1I\"},\"artists\":[{\"external_urls\":{\"spotify\":\"https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4\"},\"href\":\"https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4\",\"id\":\"3TVXtAsR1Inumwj472S9r4\",\"name\":\"Drake\",\"type\":\"artist\",\"uri\":\"spotify:artist:3TVXtAsR1Inumwj472S9r4\"}],\"available_markets\":[\"CA\",\"MX\",\"US\"],\"disc_number\":1,\"duration_ms\":241853,\"explicit\":true,\"external_ids\":{\"isrc\":\"USCM51500010\"},\"external_urls\":{\"spotify\":\"https://open.spotify.com/track/1ID1QFSNNxi0hiZCNcwjUC\"},\"href\":\"https://api.spotify.com/v1/tracks/1ID1QFSNNxi0hiZCNcwjUC\",\"id\":\"1ID1QFSNNxi0hiZCNcwjUC\",\"name\":\"Legend\",\"popularity\":72,\"preview_url\":\"https://p.scdn.co/mp3-preview/34fe00d7d951e42017bbbd8a424244c3cf1006e1?cid=null\",\"track_number\":1,\"type\":\"track\",\"uri\":\"spotify:track:1ID1QFSNNxi0hiZCNcwjUC\"}]}")

##Exploring the structure of the JSON:

#print(type(data)) #Dict

#print(data.keys()) #['tracks']

#print(len(data['tracks'])) #10 tracks

# print(data['tracks'][0].keys()) #['album', 'artists', 'available_markets', 'disc_number', 'duration_ms', 'explicit', 'external_ids', 'external_urls', 'href', 'id', 'name', 'popularity', 'preview_url', 'track_number', 'type', 'uri']

# print(data['tracks'][0]['album'].keys()) #'album_type', 'artists', 'available_markets', 'external_urls', 'href', 'id', 'images', 'name', 'type', 'uri'

# print(data['tracks'][0]['album']['artists']) #{'external_urls': {'spotify': 'https://open.spotify.com/artist/3TVXtAsR1Inumwj472S9r4'}, 'href': 'https://api.spotify.com/v1/artists/3TVXtAsR1Inumwj472S9r4', 'id': '3TVXtAsR1Inumwj472S9r4', 'name': 'Drake', 'type': 'artist', 'uri': 'spotify:artist:3TVXtAsR1Inumwj472S9r4'}

# print(data['tracks'][0]['album']['artists'][0].keys()) #['external_urls', 'href', 'id', 'name', 'type', 'uri']

# print(data['tracks'][0]['album']['artists'][0]['name']) #Drake



##Answering the questions

#1. How many songs are there?

print(len(data['tracks'])) #10 tracks

#2. List the name of each song, along with its popularity.

# print(data['tracks'][0]['name'])
# print(data['tracks'][2]['name'])
# print(data['tracks'][9]['name'])

tracks = data['tracks']

for track in tracks:
    print("Name:", track['name'])
    print("Popularity:", track['popularity'])

#3. How long would it take, in minutes, to listen to all of these songs in a row?

#I'm assuming that duration_ms = duration in milliseconds 

#print(tracks[0]['duration_ms']) #207813 milliseconds, which matches up with the length of 'Fake Love' by Drake. 

count_ms = 0

for track in tracks:
#    print(track['duration_ms'])
    count_ms = count_ms + track['duration_ms']

print("total time:", count_ms/1000/60, "minutes")

#4. For each song, list every artist that worked on it.

#print(tracks[1]['artists'][0]['name'])
#print(tracks[1]['artists'][1]['name'])

count = 1

for track in tracks:
    print("Artists on track", count)
    for artist in track['artists']:
        print(artist['name'])
    count = count + 1

#5. For each song, list every musician that worked on it EXCEPT Drake

#Original solution -- worked but the output looked janky 

# count = 1

# for track in tracks:
#     print("Artists besides Drake on track", count)
#     for artist in track['artists']:
#         if artist['name'] == 'Drake':
#             print("")
#         else:
#             print(artist['name'])
#     count = count + 1

#Solution from homework:
# for track in tracks:
#   print("Song name:", track['name'])
#   for artist in track['artists']:
#     if artist['name'] != 'Drake':
#       print("  -", artist['name'])


#Solution with help of Ed

#print(len(tracks[0]['artists']))
#print(len(tracks[1]['artists']))
#print(len(tracks[2]['artists']))

count = 1

for track in tracks:
    print("Artists besides Drake on track", count,":")
    for artist in track['artists']:
        if len(track['artists']) == 1 and artist['name'] == 'Drake':
            print("No one")
        else:
            if artist['name'] == 'Drake':
                continue
            else:
                print(artist['name'])
    count = count + 1

#6. How many songs are from albums, and how many are from singles?

single_count = 0
album_count = 0

for track in tracks:
    print(track['album']['album_type'])
    if track['album']['album_type'] == 'single':
        single_count = single_count + 1
    else:
        album_count = album_count + 1

print("There are", single_count, "songs from singles and", album_count, "songs from albums.")

#7. What percentage of these songs are marked as explicit?

explicit_count = 0

for track in tracks:
    print(track['explicit'])
    if track['explicit'] == True:
        explicit_count = explicit_count + 1

print(explicit_count*10, "percent of songs are explicit")

#8. I'd like to listen to one of the songs! Is there maybe a URL where I can listen to it?

count = 1

for track in tracks:
    print("Song", count)
    print(track['album']['external_urls']['spotify'])
    count = count + 1

print("🍌🍌🍌🍌🍌🍌")

#9. What is the most popular song?

largest_rating = tracks[1]['popularity']
most_popular = tracks[1]['name']

for track in tracks:
     print("Name:", track['name'])
     print("Popularity:", track['popularity'])
     if track['popularity'] > largest_rating:
         largest_rating = track['popularity']
         most_popular = track['name']

print("The most popular song is", most_popular, "with a rating of", largest_rating)

#Could we also use a for loop to create a dictionary and then sort the dictionary by popularity? 
#I asked Ed: Yes, but the original solution is better because it uses less memory. 

#Alternative solution:

#https://stackoverflow.com/questions/19121722/build-dictionary-in-python-loop-list-and-dictionary-comprehensions
#https://www.geeksforgeeks.org/python-convert-two-lists-into-a-dictionary/
#https://stackabuse.com/how-to-sort-dictionary-by-value-in-python

# names = []
# popularity = []

# for track in tracks:
#      print("Name:", track['name'])
#      print("Popularity:", track['popularity'])
#      names.append(track['name'])
#      popularity.append(track['popularity'])

# popularity_dict = dict(zip(names, popularity))

# print(names)
# print(popularity)
# print(popularity_dict)
# As it happens, the songs were in popularity order anyway 

#Alternative solution from homework using lambda:

# sorted_songs = sorted(tracks, key=lambda song: song['popularity']) 
# most_popular = sorted_songs[-1]
# print("The most popular song is", most_popular['name'])