# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilireq.grpc.protos.bilibili/app/playurl/v1/playurl.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n%bilibili/app/playurl/v1/playurl.proto\x12\x17\x62ilibili.app.playurl.v1\"D\n\x02\x41\x42\x12/\n\x06glance\x18\x01 \x01(\x0b\x32\x1f.bilibili.app.playurl.v1.Glance\x12\r\n\x05group\x18\x02 \x01(\x05\"m\n\x07\x41rcConf\x12\x12\n\nis_support\x18\x01 \x01(\x08\x12\x10\n\x08\x64isabled\x18\x02 \x01(\x08\x12<\n\rextra_content\x18\x03 \x01(\x0b\x32%.bilibili.app.playurl.v1.ExtraContent\"$\n\x07\x43hronos\x12\x0b\n\x03md5\x18\x01 \x01(\t\x12\x0c\n\x04\x66ile\x18\x02 \x01(\t\"T\n\x0b\x42uttonStyle\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x12\n\ntext_color\x18\x02 \x01(\t\x12\x10\n\x08\x62g_color\x18\x03 \x01(\t\x12\x11\n\tjump_link\x18\x04 \x01(\t\"\xc1\x01\n\tCloudConf\x12\x0c\n\x04show\x18\x01 \x01(\x08\x12\x34\n\tconf_type\x18\x02 \x01(\x0e\x32!.bilibili.app.playurl.v1.ConfType\x12\x38\n\x0b\x66ield_value\x18\x03 \x01(\x0b\x32#.bilibili.app.playurl.v1.FieldValue\x12\x36\n\nconf_value\x18\x04 \x01(\x0b\x32\".bilibili.app.playurl.v1.ConfValue\"B\n\tConfValue\x12\x14\n\nswitch_val\x18\x01 \x01(\x08H\x00\x12\x16\n\x0cselected_val\x18\x02 \x01(\x03H\x00\x42\x07\n\x05value\"\xa5\x01\n\x08\x44\x61shItem\x12\n\n\x02id\x18\x01 \x01(\r\x12\x0f\n\x07\x62\x61seUrl\x18\x02 \x01(\t\x12\x12\n\nbackup_url\x18\x03 \x03(\t\x12\x11\n\tbandwidth\x18\x04 \x01(\r\x12\x0f\n\x07\x63odecid\x18\x05 \x01(\r\x12\x0b\n\x03md5\x18\x06 \x01(\t\x12\x0c\n\x04size\x18\x07 \x01(\x04\x12\x12\n\nframe_rate\x18\x08 \x01(\t\x12\x15\n\rwidevine_pssh\x18\t \x01(\t\"\xdf\x01\n\tDashVideo\x12\x10\n\x08\x62\x61se_url\x18\x01 \x01(\t\x12\x12\n\nbackup_url\x18\x02 \x03(\t\x12\x11\n\tbandwidth\x18\x03 \x01(\r\x12\x0f\n\x07\x63odecid\x18\x04 \x01(\r\x12\x0b\n\x03md5\x18\x05 \x01(\t\x12\x0c\n\x04size\x18\x06 \x01(\x04\x12\x0f\n\x07\x61udioId\x18\x07 \x01(\r\x12\x12\n\nno_rexcode\x18\x08 \x01(\x08\x12\x12\n\nframe_rate\x18\t \x01(\t\x12\r\n\x05width\x18\n \x01(\x05\x12\x0e\n\x06height\x18\x0b \x01(\x05\x12\x15\n\rwidevine_pssh\x18\x0c \x01(\t\"\x9d\x01\n\tDolbyItem\x12\x35\n\x04type\x18\x01 \x01(\x0e\x32\'.bilibili.app.playurl.v1.DolbyItem.Type\x12\x30\n\x05\x61udio\x18\x02 \x01(\x0b\x32!.bilibili.app.playurl.v1.DashItem\"\'\n\x04Type\x12\x08\n\x04NONE\x10\x00\x12\n\n\x06\x43OMMON\x10\x01\x12\t\n\x05\x41TMOS\x10\x02\"6\n\x05\x45vent\x12-\n\x05shake\x18\x01 \x01(\x0b\x32\x1e.bilibili.app.playurl.v1.Shake\">\n\x0c\x45xtraContent\x12\x17\n\x0f\x64isabled_reason\x18\x01 \x01(\t\x12\x15\n\rdisabled_code\x18\x02 \x01(\x03\"\'\n\nFieldValue\x12\x10\n\x06switch\x18\x01 \x01(\x08H\x00\x42\x07\n\x05value\"\x8d\x01\n\x11\x46ormatDescription\x12\x0f\n\x07quality\x18\x01 \x01(\x05\x12\x0e\n\x06\x66ormat\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x17\n\x0fnew_description\x18\x04 \x01(\t\x12\x14\n\x0c\x64isplay_desc\x18\x05 \x01(\t\x12\x13\n\x0bsuperscript\x18\x06 \x01(\t\"<\n\x06Glance\x12\x11\n\tcan_watch\x18\x01 \x01(\x08\x12\r\n\x05times\x18\x02 \x01(\x03\x12\x10\n\x08\x64uration\x18\x03 \x01(\x03\"\xc9\r\n\x0fPlayAbilityConf\x12@\n\x14\x62\x61\x63kground_play_conf\x18\x01 \x01(\x0b\x32\".bilibili.app.playurl.v1.CloudConf\x12\x35\n\tflip_conf\x18\x02 \x01(\x0b\x32\".bilibili.app.playurl.v1.CloudConf\x12\x35\n\tcast_conf\x18\x03 \x01(\x0b\x32\".bilibili.app.playurl.v1.CloudConf\x12\x39\n\rfeedback_conf\x18\x04 \x01(\x0b\x32\".bilibili.app.playurl.v1.CloudConf\x12\x39\n\rsubtitle_conf\x18\x05 \x01(\x0b\x32\".bilibili.app.playurl.v1.CloudConf\x12>\n\x12playback_rate_conf\x18\x06 \x01(\x0b\x32\".bilibili.app.playurl.v1.CloudConf\x12\x38\n\x0ctime_up_conf\x18\x07 \x01(\x0b\x32\".bilibili.app.playurl.v1.CloudConf\x12>\n\x12playback_mode_conf\x18\x08 \x01(\x0b\x32\".bilibili.app.playurl.v1.CloudConf\x12;\n\x0fscale_mode_conf\x18\t \x01(\x0b\x32\".bilibili.app.playurl.v1.CloudConf\x12\x35\n\tlike_conf\x18\n \x01(\x0b\x32\".bilibili.app.playurl.v1.CloudConf\x12\x38\n\x0c\x64islike_conf\x18\x0b \x01(\x0b\x32\".bilibili.app.playurl.v1.CloudConf\x12\x35\n\tcoin_conf\x18\x0c \x01(\x0b\x32\".bilibili.app.playurl.v1.CloudConf\x12\x35\n\telec_conf\x18\r \x01(\x0b\x32\".bilibili.app.playurl.v1.CloudConf\x12\x36\n\nshare_conf\x18\x0e \x01(\x0b\x32\".bilibili.app.playurl.v1.CloudConf\x12<\n\x10screen_shot_conf\x18\x0f \x01(\x0b\x32\".bilibili.app.playurl.v1.CloudConf\x12<\n\x10lock_screen_conf\x18\x10 \x01(\x0b\x32\".bilibili.app.playurl.v1.CloudConf\x12:\n\x0erecommend_conf\x18\x11 \x01(\x0b\x32\".bilibili.app.playurl.v1.CloudConf\x12?\n\x13playback_speed_conf\x18\x12 \x01(\x0b\x32\".bilibili.app.playurl.v1.CloudConf\x12;\n\x0f\x64\x65\x66inition_conf\x18\x13 \x01(\x0b\x32\".bilibili.app.playurl.v1.CloudConf\x12;\n\x0fselections_conf\x18\x14 \x01(\x0b\x32\".bilibili.app.playurl.v1.CloudConf\x12\x35\n\tnext_conf\x18\x15 \x01(\x0b\x32\".bilibili.app.playurl.v1.CloudConf\x12\x38\n\x0c\x65\x64it_dm_conf\x18\x16 \x01(\x0b\x32\".bilibili.app.playurl.v1.CloudConf\x12=\n\x11small_window_conf\x18\x17 \x01(\x0b\x32\".bilibili.app.playurl.v1.CloudConf\x12\x36\n\nshake_conf\x18\x18 \x01(\x0b\x32\".bilibili.app.playurl.v1.CloudConf\x12\x39\n\router_dm_conf\x18\x19 \x01(\x0b\x32\".bilibili.app.playurl.v1.CloudConf\x12:\n\x0einnerDmDisable\x18\x1a \x01(\x0b\x32\".bilibili.app.playurl.v1.CloudConf\x12\x39\n\rinner_dm_conf\x18\x1b \x01(\x0b\x32\".bilibili.app.playurl.v1.CloudConf\x12\x36\n\ndolby_conf\x18\x1c \x01(\x0b\x32\".bilibili.app.playurl.v1.CloudConf\x12=\n\x11\x63olor_filter_conf\x18\x1d \x01(\x0b\x32\".bilibili.app.playurl.v1.CloudConf\"\xcb\r\n\x0bPlayArcConf\x12>\n\x14\x62\x61\x63kground_play_conf\x18\x01 \x01(\x0b\x32 .bilibili.app.playurl.v1.ArcConf\x12\x33\n\tflip_conf\x18\x02 \x01(\x0b\x32 .bilibili.app.playurl.v1.ArcConf\x12\x33\n\tcast_conf\x18\x03 \x01(\x0b\x32 .bilibili.app.playurl.v1.ArcConf\x12\x37\n\rfeedback_conf\x18\x04 \x01(\x0b\x32 .bilibili.app.playurl.v1.ArcConf\x12\x37\n\rsubtitle_conf\x18\x05 \x01(\x0b\x32 .bilibili.app.playurl.v1.ArcConf\x12<\n\x12playback_rate_conf\x18\x06 \x01(\x0b\x32 .bilibili.app.playurl.v1.ArcConf\x12\x36\n\x0ctime_up_conf\x18\x07 \x01(\x0b\x32 .bilibili.app.playurl.v1.ArcConf\x12<\n\x12playback_mode_conf\x18\x08 \x01(\x0b\x32 .bilibili.app.playurl.v1.ArcConf\x12\x39\n\x0fscale_mode_conf\x18\t \x01(\x0b\x32 .bilibili.app.playurl.v1.ArcConf\x12\x33\n\tlike_conf\x18\n \x01(\x0b\x32 .bilibili.app.playurl.v1.ArcConf\x12\x36\n\x0c\x64islike_conf\x18\x0b \x01(\x0b\x32 .bilibili.app.playurl.v1.ArcConf\x12\x33\n\tcoin_conf\x18\x0c \x01(\x0b\x32 .bilibili.app.playurl.v1.ArcConf\x12\x33\n\telec_conf\x18\r \x01(\x0b\x32 .bilibili.app.playurl.v1.ArcConf\x12\x34\n\nshare_conf\x18\x0e \x01(\x0b\x32 .bilibili.app.playurl.v1.ArcConf\x12:\n\x10screen_shot_conf\x18\x0f \x01(\x0b\x32 .bilibili.app.playurl.v1.ArcConf\x12:\n\x10lock_screen_conf\x18\x10 \x01(\x0b\x32 .bilibili.app.playurl.v1.ArcConf\x12\x38\n\x0erecommend_conf\x18\x11 \x01(\x0b\x32 .bilibili.app.playurl.v1.ArcConf\x12=\n\x13playback_speed_conf\x18\x12 \x01(\x0b\x32 .bilibili.app.playurl.v1.ArcConf\x12\x39\n\x0f\x64\x65\x66inition_conf\x18\x13 \x01(\x0b\x32 .bilibili.app.playurl.v1.ArcConf\x12\x39\n\x0fselections_conf\x18\x14 \x01(\x0b\x32 .bilibili.app.playurl.v1.ArcConf\x12\x33\n\tnext_conf\x18\x15 \x01(\x0b\x32 .bilibili.app.playurl.v1.ArcConf\x12\x36\n\x0c\x65\x64it_dm_conf\x18\x16 \x01(\x0b\x32 .bilibili.app.playurl.v1.ArcConf\x12;\n\x11small_window_conf\x18\x17 \x01(\x0b\x32 .bilibili.app.playurl.v1.ArcConf\x12\x34\n\nshake_conf\x18\x18 \x01(\x0b\x32 .bilibili.app.playurl.v1.ArcConf\x12\x37\n\router_dm_conf\x18\x19 \x01(\x0b\x32 .bilibili.app.playurl.v1.ArcConf\x12\x37\n\rinner_dm_conf\x18\x1a \x01(\x0b\x32 .bilibili.app.playurl.v1.ArcConf\x12\x37\n\rpanorama_conf\x18\x1b \x01(\x0b\x32 .bilibili.app.playurl.v1.ArcConf\x12\x34\n\ndolby_conf\x18\x1c \x01(\x0b\x32 .bilibili.app.playurl.v1.ArcConf\x12?\n\x15screen_recording_conf\x18\x1d \x01(\x0b\x32 .bilibili.app.playurl.v1.ArcConf\x12;\n\x11\x63olor_filter_conf\x18\x1e \x01(\x0b\x32 .bilibili.app.playurl.v1.ArcConf\"\x13\n\x11PlayConfEditReply\"L\n\x0fPlayConfEditReq\x12\x39\n\tplay_conf\x18\x01 \x03(\x0b\x32&.bilibili.app.playurl.v1.PlayConfState\"L\n\rPlayConfReply\x12;\n\tplay_conf\x18\x01 \x01(\x0b\x32(.bilibili.app.playurl.v1.PlayAbilityConf\"\r\n\x0bPlayConfReq\"\xc5\x01\n\rPlayConfState\x12\x34\n\tconf_type\x18\x01 \x01(\x0e\x32!.bilibili.app.playurl.v1.ConfType\x12\x0c\n\x04show\x18\x02 \x01(\x08\x12\x38\n\x0b\x66ield_value\x18\x03 \x01(\x0b\x32#.bilibili.app.playurl.v1.FieldValue\x12\x36\n\nconf_value\x18\x04 \x01(\x0b\x32\".bilibili.app.playurl.v1.ConfValue\"\x9d\x01\n\tPlayLimit\x12\x34\n\x04\x63ode\x18\x01 \x01(\x0e\x32&.bilibili.app.playurl.v1.PlayLimitCode\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\x13\n\x0bsub_message\x18\x03 \x01(\t\x12\x34\n\x06\x62utton\x18\x04 \x01(\x0b\x32$.bilibili.app.playurl.v1.ButtonStyle\"\xc1\x03\n\x0cPlayURLReply\x12\x0f\n\x07quality\x18\x01 \x01(\r\x12\x0e\n\x06\x66ormat\x18\x02 \x01(\t\x12\x12\n\ntimelength\x18\x03 \x01(\x04\x12\x15\n\rvideo_codecid\x18\x04 \x01(\r\x12\r\n\x05\x66nver\x18\x05 \x01(\r\x12\r\n\x05\x66nval\x18\x06 \x01(\r\x12\x15\n\rvideo_project\x18\x07 \x01(\x08\x12\x32\n\x04\x64url\x18\x08 \x03(\x0b\x32$.bilibili.app.playurl.v1.ResponseUrl\x12\x33\n\x04\x64\x61sh\x18\t \x01(\x0b\x32%.bilibili.app.playurl.v1.ResponseDash\x12\x12\n\nno_rexcode\x18\n \x01(\x05\x12<\n\rupgrade_limit\x18\x0b \x01(\x0b\x32%.bilibili.app.playurl.v1.UpgradeLimit\x12\x43\n\x0fsupport_formats\x18\x0c \x03(\x0b\x32*.bilibili.app.playurl.v1.FormatDescription\x12\x30\n\x04type\x18\r \x01(\x0e\x32\".bilibili.app.playurl.v1.VideoType\"\xa8\x01\n\nPlayURLReq\x12\x0b\n\x03\x61id\x18\x01 \x01(\x03\x12\x0b\n\x03\x63id\x18\x02 \x01(\x03\x12\n\n\x02qn\x18\x03 \x01(\x03\x12\r\n\x05\x66nver\x18\x04 \x01(\x05\x12\r\n\x05\x66nval\x18\x05 \x01(\x05\x12\x10\n\x08\x64ownload\x18\x06 \x01(\r\x12\x12\n\nforce_host\x18\x07 \x01(\x05\x12\r\n\x05\x66ourk\x18\x08 \x01(\x08\x12\r\n\x05spmid\x18\t \x01(\t\x12\x12\n\nfrom_spmid\x18\n \x01(\t\"\xbd\x03\n\rPlayViewReply\x12\x36\n\nvideo_info\x18\x01 \x01(\x0b\x32\".bilibili.app.playurl.v1.VideoInfo\x12;\n\tplay_conf\x18\x02 \x01(\x0b\x32(.bilibili.app.playurl.v1.PlayAbilityConf\x12<\n\rupgrade_limit\x18\x03 \x01(\x0b\x32%.bilibili.app.playurl.v1.UpgradeLimit\x12\x31\n\x07\x63hronos\x18\x04 \x01(\x0b\x32 .bilibili.app.playurl.v1.Chronos\x12\x36\n\x08play_arc\x18\x05 \x01(\x0b\x32$.bilibili.app.playurl.v1.PlayArcConf\x12-\n\x05\x65vent\x18\x06 \x01(\x0b\x32\x1e.bilibili.app.playurl.v1.Event\x12\'\n\x02\x61\x62\x18\x07 \x01(\x0b\x32\x1b.bilibili.app.playurl.v1.AB\x12\x36\n\nplay_limit\x18\x08 \x01(\x0b\x32\".bilibili.app.playurl.v1.PlayLimit\"\xcb\x02\n\x0bPlayViewReq\x12\x0b\n\x03\x61id\x18\x01 \x01(\x03\x12\x0b\n\x03\x63id\x18\x02 \x01(\x03\x12\n\n\x02qn\x18\x03 \x01(\x03\x12\r\n\x05\x66nver\x18\x04 \x01(\x05\x12\r\n\x05\x66nval\x18\x05 \x01(\x05\x12\x10\n\x08\x64ownload\x18\x06 \x01(\r\x12\x12\n\nforce_host\x18\x07 \x01(\x05\x12\r\n\x05\x66ourk\x18\x08 \x01(\x08\x12\r\n\x05spmid\x18\t \x01(\t\x12\x12\n\nfrom_spmid\x18\n \x01(\t\x12\x16\n\x0eteenagers_mode\x18\x0b \x01(\x05\x12<\n\x11prefer_codec_type\x18\x0c \x01(\x0e\x32!.bilibili.app.playurl.v1.CodeType\x12\x33\n\x08\x62usiness\x18\r \x01(\x0e\x32!.bilibili.app.playurl.v1.Business\x12\x15\n\rvoice_balance\x18\x0e \x01(\x03\"F\n\x0cProjectReply\x12\x36\n\x07project\x18\x01 \x01(\x0b\x32%.bilibili.app.playurl.v1.PlayURLReply\"\xcf\x01\n\nProjectReq\x12\x0b\n\x03\x61id\x18\x01 \x01(\x03\x12\x0b\n\x03\x63id\x18\x02 \x01(\x03\x12\n\n\x02qn\x18\x03 \x01(\x03\x12\r\n\x05\x66nver\x18\x04 \x01(\x05\x12\r\n\x05\x66nval\x18\x05 \x01(\x05\x12\x10\n\x08\x64ownload\x18\x06 \x01(\r\x12\x12\n\nforce_host\x18\x07 \x01(\x05\x12\r\n\x05\x66ourk\x18\x08 \x01(\x08\x12\r\n\x05spmid\x18\t \x01(\t\x12\x12\n\nfrom_spmid\x18\n \x01(\t\x12\x10\n\x08protocol\x18\x0b \x01(\x05\x12\x13\n\x0b\x64\x65vice_type\x18\x0c \x01(\x05\"r\n\x0cResponseDash\x12\x30\n\x05video\x18\x01 \x03(\x0b\x32!.bilibili.app.playurl.v1.DashItem\x12\x30\n\x05\x61udio\x18\x02 \x03(\x0b\x32!.bilibili.app.playurl.v1.DashItem\"h\n\x0bResponseUrl\x12\r\n\x05order\x18\x01 \x01(\r\x12\x0e\n\x06length\x18\x02 \x01(\x04\x12\x0c\n\x04size\x18\x03 \x01(\x04\x12\x0b\n\x03url\x18\x04 \x01(\t\x12\x12\n\nbackup_url\x18\x05 \x03(\t\x12\x0b\n\x03md5\x18\x06 \x01(\t\"E\n\x0cSegmentVideo\x12\x35\n\x07segment\x18\x01 \x03(\x0b\x32$.bilibili.app.playurl.v1.ResponseUrl\"\x15\n\x05Shake\x12\x0c\n\x04\x66ile\x18\x01 \x01(\t\"\xc7\x01\n\x06Stream\x12\x38\n\x0bstream_info\x18\x01 \x01(\x0b\x32#.bilibili.app.playurl.v1.StreamInfo\x12\x38\n\ndash_video\x18\x02 \x01(\x0b\x32\".bilibili.app.playurl.v1.DashVideoH\x00\x12>\n\rsegment_video\x18\x03 \x01(\x0b\x32%.bilibili.app.playurl.v1.SegmentVideoH\x00\x42\t\n\x07\x63ontent\"\xcc\x02\n\nStreamInfo\x12\x0f\n\x07quality\x18\x01 \x01(\r\x12\x0e\n\x06\x66ormat\x18\x02 \x01(\t\x12\x13\n\x0b\x64\x65scription\x18\x03 \x01(\t\x12\x32\n\x08\x65rr_code\x18\x04 \x01(\x0e\x32 .bilibili.app.playurl.v1.PlayErr\x12\x33\n\x05limit\x18\x05 \x01(\x0b\x32$.bilibili.app.playurl.v1.StreamLimit\x12\x10\n\x08need_vip\x18\x06 \x01(\x08\x12\x12\n\nneed_login\x18\x07 \x01(\x08\x12\x0e\n\x06intact\x18\x08 \x01(\x08\x12\x12\n\nno_rexcode\x18\t \x01(\x08\x12\x11\n\tattribute\x18\n \x01(\x03\x12\x17\n\x0fnew_description\x18\x0b \x01(\t\x12\x14\n\x0c\x64isplay_desc\x18\x0c \x01(\t\x12\x13\n\x0bsuperscript\x18\r \x01(\t\"6\n\x0bStreamLimit\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0b\n\x03uri\x18\x02 \x01(\t\x12\x0b\n\x03msg\x18\x03 \x01(\t\",\n\rUpgradeButton\x12\r\n\x05title\x18\x01 \x01(\t\x12\x0c\n\x04link\x18\x02 \x01(\t\"t\n\x0cUpgradeLimit\x12\x0c\n\x04\x63ode\x18\x01 \x01(\x05\x12\x0f\n\x07message\x18\x02 \x01(\t\x12\r\n\x05image\x18\x03 \x01(\t\x12\x36\n\x06\x62utton\x18\x04 \x01(\x0b\x32&.bilibili.app.playurl.v1.UpgradeButton\"\xac\x02\n\tVideoInfo\x12\x0f\n\x07quality\x18\x01 \x01(\r\x12\x0e\n\x06\x66ormat\x18\x02 \x01(\t\x12\x12\n\ntimelength\x18\x03 \x01(\x04\x12\x15\n\rvideo_codecid\x18\x04 \x01(\r\x12\x34\n\x0bstream_list\x18\x05 \x03(\x0b\x32\x1f.bilibili.app.playurl.v1.Stream\x12\x35\n\ndash_audio\x18\x06 \x03(\x0b\x32!.bilibili.app.playurl.v1.DashItem\x12\x31\n\x05\x64olby\x18\x07 \x01(\x0b\x32\".bilibili.app.playurl.v1.DolbyItem\x12\x33\n\x06volume\x18\x08 \x01(\x0b\x32#.bilibili.app.playurl.v1.VolumeInfo\"\xa3\x01\n\nVolumeInfo\x12\x12\n\nmeasured_i\x18\x01 \x01(\x01\x12\x14\n\x0cmeasured_lra\x18\x02 \x01(\x01\x12\x13\n\x0bmeasured_tp\x18\x03 \x01(\x01\x12\x1a\n\x12measured_threshold\x18\x04 \x01(\x01\x12\x15\n\rtarget_offset\x18\x05 \x01(\x01\x12\x10\n\x08target_i\x18\x06 \x01(\x01\x12\x11\n\ttarget_tp\x18\x07 \x01(\x01*\"\n\x08\x42usiness\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05STORY\x10\x01*=\n\x08\x43odeType\x12\n\n\x06NOCODE\x10\x00\x12\x0b\n\x07\x43ODE264\x10\x01\x12\x0b\n\x07\x43ODE265\x10\x02\x12\x0b\n\x07\x43ODEAV1\x10\x03*\xaf\x03\n\x08\x43onfType\x12\n\n\x06NoType\x10\x00\x12\x0c\n\x08\x46LIPCONF\x10\x01\x12\x0c\n\x08\x43\x41STCONF\x10\x02\x12\x0c\n\x08\x46\x45\x45\x44\x42\x41\x43K\x10\x03\x12\x0c\n\x08SUBTITLE\x10\x04\x12\x10\n\x0cPLAYBACKRATE\x10\x05\x12\n\n\x06TIMEUP\x10\x06\x12\x10\n\x0cPLAYBACKMODE\x10\x07\x12\r\n\tSCALEMODE\x10\x08\x12\x12\n\x0e\x42\x41\x43KGROUNDPLAY\x10\t\x12\x08\n\x04LIKE\x10\n\x12\x0b\n\x07\x44ISLIKE\x10\x0b\x12\x08\n\x04\x43OIN\x10\x0c\x12\x08\n\x04\x45LEC\x10\r\x12\t\n\x05SHARE\x10\x0e\x12\x0e\n\nSCREENSHOT\x10\x0f\x12\x0e\n\nLOCKSCREEN\x10\x10\x12\r\n\tRECOMMEND\x10\x11\x12\x11\n\rPLAYBACKSPEED\x10\x12\x12\x0e\n\nDEFINITION\x10\x13\x12\x0e\n\nSELECTIONS\x10\x14\x12\x08\n\x04NEXT\x10\x15\x12\n\n\x06\x45\x44ITDM\x10\x16\x12\x0f\n\x0bSMALLWINDOW\x10\x17\x12\t\n\x05SHAKE\x10\x18\x12\x0b\n\x07OUTERDM\x10\x19\x12\x0b\n\x07INNERDM\x10\x1a\x12\x0c\n\x08PANORAMA\x10\x1b\x12\t\n\x05\x44OLBY\x10\x1c\x12\x0f\n\x0b\x43OLORFILTER\x10\x1d*.\n\x05Group\x12\x10\n\x0cUnknownGroup\x10\x00\x12\x05\n\x01\x41\x10\x01\x12\x05\n\x01\x42\x10\x02\x12\x05\n\x01\x43\x10\x03*1\n\x07PlayErr\x12\t\n\x05NoErr\x10\x00\x12\x1b\n\x17WithMultiDeviceLoginErr\x10\x01*2\n\rPlayLimitCode\x12\r\n\tPLCUnkown\x10\x00\x12\x12\n\x0ePLCUgcNotPayed\x10\x01*L\n\tVideoType\x12\x11\n\rUnknown_VALUE\x10\x00\x12\r\n\tFLV_VALUE\x10\x01\x12\x0e\n\nDASH_VALUE\x10\x02\x12\r\n\tMP4_VALUE\x10\x03\x32\xd1\x03\n\x07PlayURL\x12U\n\x07PlayURL\x12#.bilibili.app.playurl.v1.PlayURLReq\x1a%.bilibili.app.playurl.v1.PlayURLReply\x12U\n\x07Project\x12#.bilibili.app.playurl.v1.ProjectReq\x1a%.bilibili.app.playurl.v1.ProjectReply\x12X\n\x08PlayView\x12$.bilibili.app.playurl.v1.PlayViewReq\x1a&.bilibili.app.playurl.v1.PlayViewReply\x12\x64\n\x0cPlayConfEdit\x12(.bilibili.app.playurl.v1.PlayConfEditReq\x1a*.bilibili.app.playurl.v1.PlayConfEditReply\x12X\n\x08PlayConf\x12$.bilibili.app.playurl.v1.PlayConfReq\x1a&.bilibili.app.playurl.v1.PlayConfReplyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bilibili.app.playurl.v1.playurl_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_BUSINESS']._serialized_start=8819
  _globals['_BUSINESS']._serialized_end=8853
  _globals['_CODETYPE']._serialized_start=8855
  _globals['_CODETYPE']._serialized_end=8916
  _globals['_CONFTYPE']._serialized_start=8919
  _globals['_CONFTYPE']._serialized_end=9350
  _globals['_GROUP']._serialized_start=9352
  _globals['_GROUP']._serialized_end=9398
  _globals['_PLAYERR']._serialized_start=9400
  _globals['_PLAYERR']._serialized_end=9449
  _globals['_PLAYLIMITCODE']._serialized_start=9451
  _globals['_PLAYLIMITCODE']._serialized_end=9501
  _globals['_VIDEOTYPE']._serialized_start=9503
  _globals['_VIDEOTYPE']._serialized_end=9579
  _globals['_AB']._serialized_start=66
  _globals['_AB']._serialized_end=134
  _globals['_ARCCONF']._serialized_start=136
  _globals['_ARCCONF']._serialized_end=245
  _globals['_CHRONOS']._serialized_start=247
  _globals['_CHRONOS']._serialized_end=283
  _globals['_BUTTONSTYLE']._serialized_start=285
  _globals['_BUTTONSTYLE']._serialized_end=369
  _globals['_CLOUDCONF']._serialized_start=372
  _globals['_CLOUDCONF']._serialized_end=565
  _globals['_CONFVALUE']._serialized_start=567
  _globals['_CONFVALUE']._serialized_end=633
  _globals['_DASHITEM']._serialized_start=636
  _globals['_DASHITEM']._serialized_end=801
  _globals['_DASHVIDEO']._serialized_start=804
  _globals['_DASHVIDEO']._serialized_end=1027
  _globals['_DOLBYITEM']._serialized_start=1030
  _globals['_DOLBYITEM']._serialized_end=1187
  _globals['_DOLBYITEM_TYPE']._serialized_start=1148
  _globals['_DOLBYITEM_TYPE']._serialized_end=1187
  _globals['_EVENT']._serialized_start=1189
  _globals['_EVENT']._serialized_end=1243
  _globals['_EXTRACONTENT']._serialized_start=1245
  _globals['_EXTRACONTENT']._serialized_end=1307
  _globals['_FIELDVALUE']._serialized_start=1309
  _globals['_FIELDVALUE']._serialized_end=1348
  _globals['_FORMATDESCRIPTION']._serialized_start=1351
  _globals['_FORMATDESCRIPTION']._serialized_end=1492
  _globals['_GLANCE']._serialized_start=1494
  _globals['_GLANCE']._serialized_end=1554
  _globals['_PLAYABILITYCONF']._serialized_start=1557
  _globals['_PLAYABILITYCONF']._serialized_end=3294
  _globals['_PLAYARCCONF']._serialized_start=3297
  _globals['_PLAYARCCONF']._serialized_end=5036
  _globals['_PLAYCONFEDITREPLY']._serialized_start=5038
  _globals['_PLAYCONFEDITREPLY']._serialized_end=5057
  _globals['_PLAYCONFEDITREQ']._serialized_start=5059
  _globals['_PLAYCONFEDITREQ']._serialized_end=5135
  _globals['_PLAYCONFREPLY']._serialized_start=5137
  _globals['_PLAYCONFREPLY']._serialized_end=5213
  _globals['_PLAYCONFREQ']._serialized_start=5215
  _globals['_PLAYCONFREQ']._serialized_end=5228
  _globals['_PLAYCONFSTATE']._serialized_start=5231
  _globals['_PLAYCONFSTATE']._serialized_end=5428
  _globals['_PLAYLIMIT']._serialized_start=5431
  _globals['_PLAYLIMIT']._serialized_end=5588
  _globals['_PLAYURLREPLY']._serialized_start=5591
  _globals['_PLAYURLREPLY']._serialized_end=6040
  _globals['_PLAYURLREQ']._serialized_start=6043
  _globals['_PLAYURLREQ']._serialized_end=6211
  _globals['_PLAYVIEWREPLY']._serialized_start=6214
  _globals['_PLAYVIEWREPLY']._serialized_end=6659
  _globals['_PLAYVIEWREQ']._serialized_start=6662
  _globals['_PLAYVIEWREQ']._serialized_end=6993
  _globals['_PROJECTREPLY']._serialized_start=6995
  _globals['_PROJECTREPLY']._serialized_end=7065
  _globals['_PROJECTREQ']._serialized_start=7068
  _globals['_PROJECTREQ']._serialized_end=7275
  _globals['_RESPONSEDASH']._serialized_start=7277
  _globals['_RESPONSEDASH']._serialized_end=7391
  _globals['_RESPONSEURL']._serialized_start=7393
  _globals['_RESPONSEURL']._serialized_end=7497
  _globals['_SEGMENTVIDEO']._serialized_start=7499
  _globals['_SEGMENTVIDEO']._serialized_end=7568
  _globals['_SHAKE']._serialized_start=7570
  _globals['_SHAKE']._serialized_end=7591
  _globals['_STREAM']._serialized_start=7594
  _globals['_STREAM']._serialized_end=7793
  _globals['_STREAMINFO']._serialized_start=7796
  _globals['_STREAMINFO']._serialized_end=8128
  _globals['_STREAMLIMIT']._serialized_start=8130
  _globals['_STREAMLIMIT']._serialized_end=8184
  _globals['_UPGRADEBUTTON']._serialized_start=8186
  _globals['_UPGRADEBUTTON']._serialized_end=8230
  _globals['_UPGRADELIMIT']._serialized_start=8232
  _globals['_UPGRADELIMIT']._serialized_end=8348
  _globals['_VIDEOINFO']._serialized_start=8351
  _globals['_VIDEOINFO']._serialized_end=8651
  _globals['_VOLUMEINFO']._serialized_start=8654
  _globals['_VOLUMEINFO']._serialized_end=8817
  _globals['_PLAYURL']._serialized_start=9582
  _globals['_PLAYURL']._serialized_end=10047
# @@protoc_insertion_point(module_scope)
