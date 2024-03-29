# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: bilireq.grpc.protos.bilibili/app/viewunite/v1/viewunite.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from bilireq.grpc.protos.bilibili.app.archive.middleware.v1 import preload_pb2 as bilibili_dot_app_dot_archive_dot_middleware_dot_v1_dot_preload__pb2
from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n)bilibili/app/viewunite/v1/viewunite.proto\x12\x19\x62ilibili.app.viewunite.v1\x1a\x30\x62ilibili/app/archive/middleware/v1/preload.proto\x1a\x19google/protobuf/any.proto\"G\n\rAttentionCard\x12\x36\n\tshow_time\x18\x01 \x03(\x0b\x32#.bilibili.app.viewunite.v1.ShowTime\"\xb5\x01\n\tBadgeType\x12\x0c\n\x04text\x18\x01 \x01(\t\x12\x12\n\ntext_color\x18\x02 \x01(\t\x12\x18\n\x10text_color_night\x18\x03 \x01(\t\x12\x10\n\x08\x62g_color\x18\x04 \x01(\t\x12\x16\n\x0e\x62g_color_night\x18\x05 \x01(\t\x12\x14\n\x0c\x62order_color\x18\x06 \x01(\t\x12\x1a\n\x12\x62order_color_night\x18\x07 \x01(\t\x12\x10\n\x08\x62g_style\x18\x08 \x01(\x05\"(\n\x13\x42izFollowVideoParam\x12\x11\n\tseason_id\x18\x01 \x01(\x03\"\x1f\n\x10\x42izJumpLinkParam\x12\x0b\n\x03url\x18\x01 \x01(\t\"k\n\x17\x42izReserveActivityParam\x12\x13\n\x0b\x61\x63tivity_id\x18\x01 \x01(\x03\x12\x0c\n\x04\x66rom\x18\x02 \x01(\t\x12\x0c\n\x04type\x18\x03 \x01(\t\x12\x0b\n\x03oid\x18\x04 \x01(\x03\x12\x12\n\nreserve_id\x18\x05 \x01(\x03\"&\n\x13\x42izReserveGameParam\x12\x0f\n\x07game_id\x18\x01 \x01(\x03\"2\n\x07\x43hronos\x12\x0b\n\x03md5\x18\x01 \x01(\t\x12\x0c\n\x04\x66ile\x18\x02 \x01(\t\x12\x0c\n\x04sign\x18\x03 \x01(\t\"U\n\x0c\x43hronosParam\x12\x16\n\x0e\x65ngine_version\x18\x01 \x01(\t\x12\x18\n\x10message_protocol\x18\x02 \x01(\t\x12\x13\n\x0bservice_key\x18\x03 \x01(\t\"\xa2\x01\n\tCommandDm\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0b\n\x03oid\x18\x02 \x01(\x03\x12\x0b\n\x03mid\x18\x03 \x01(\x03\x12\x0f\n\x07\x63ommand\x18\x04 \x01(\t\x12\x0f\n\x07\x63ontent\x18\x05 \x01(\t\x12\x10\n\x08progress\x18\x06 \x01(\x05\x12\r\n\x05\x63time\x18\x07 \x01(\t\x12\r\n\x05mtime\x18\x08 \x01(\t\x12\r\n\x05\x65xtra\x18\t \x01(\t\x12\x0e\n\x06id_str\x18\n \x01(\t\"\xe5\x02\n\x0c\x43ontractCard\x12\x18\n\x10\x64isplay_progress\x18\x01 \x01(\x02\x12\x18\n\x10\x64isplay_accuracy\x18\x02 \x01(\x03\x12\x18\n\x10\x64isplay_duration\x18\x03 \x01(\x03\x12\x11\n\tshow_mode\x18\x04 \x01(\x05\x12\x11\n\tpage_type\x18\x05 \x01(\x05\x12\x34\n\x05upper\x18\x06 \x01(\x0b\x32%.bilibili.app.viewunite.v1.UpperInfos\x12\x19\n\x11is_follow_display\x18\x07 \x01(\x05\x12\x35\n\x04text\x18\x08 \x01(\x0b\x32\'.bilibili.app.viewunite.v1.ContractText\x12#\n\x1b\x66ollow_display_end_duration\x18\t \x01(\x03\x12\x17\n\x0fis_play_display\x18\n \x01(\x05\x12\x1b\n\x13is_interact_display\x18\x0b \x01(\x05\"E\n\x0c\x43ontractText\x12\r\n\x05title\x18\x01 \x01(\t\x12\x10\n\x08subtitle\x18\x02 \x01(\t\x12\x14\n\x0cinline_title\x18\x03 \x01(\t\":\n\tDimension\x12\r\n\x05width\x18\x01 \x01(\x03\x12\x0e\n\x06height\x18\x02 \x01(\x03\x12\x0e\n\x06rotate\x18\x03 \x01(\x03\"\xbd\x01\n\nDmResource\x12\x39\n\x0b\x63ommand_dms\x18\x01 \x03(\x0b\x32$.bilibili.app.viewunite.v1.CommandDm\x12;\n\tattention\x18\x02 \x01(\x0b\x32(.bilibili.app.viewunite.v1.AttentionCard\x12\x37\n\x05\x63\x61rds\x18\x03 \x03(\x0b\x32(.bilibili.app.viewunite.v1.OperationCard\"\x92\x02\n\x08Material\x12\x0c\n\x04icon\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x0b\n\x03url\x18\x03 \x01(\t\x12\x38\n\x04type\x18\x04 \x01(\x0e\x32*.bilibili.app.viewunite.v1.MaterialBizType\x12\r\n\x05param\x18\x05 \x01(\t\x12\x13\n\x0bstatic_icon\x18\x06 \x01(\t\x12\x10\n\x08\x62g_color\x18\x07 \x01(\t\x12\x0e\n\x06\x62g_pic\x18\x08 \x01(\t\x12\x11\n\tjump_type\x18\t \x01(\x05\x12\x36\n\tpage_type\x18\n \x01(\x0e\x32#.bilibili.app.viewunite.v1.PageType\x12\x12\n\nneed_login\x18\x0b \x01(\x08\"\xbb\x03\n\rOperationCard\x12\n\n\x02id\x18\x01 \x01(\x03\x12\x0c\n\x04\x66rom\x18\x02 \x01(\x05\x12\n\n\x02to\x18\x03 \x01(\x05\x12\x0e\n\x06status\x18\x04 \x01(\x08\x12\x34\n\x08\x62iz_type\x18\x05 \x01(\x0e\x32\".bilibili.app.viewunite.v1.BizType\x12@\n\x07\x63ontent\x18\x06 \x01(\x0b\x32/.bilibili.app.viewunite.v1.OperationCardContent\x12>\n\x06\x66ollow\x18\x07 \x01(\x0b\x32..bilibili.app.viewunite.v1.BizFollowVideoParam\x12\x43\n\x07reserve\x18\x08 \x01(\x0b\x32\x32.bilibili.app.viewunite.v1.BizReserveActivityParam\x12\x39\n\x04jump\x18\t \x01(\x0b\x32+.bilibili.app.viewunite.v1.BizJumpLinkParam\x12<\n\x04game\x18\n \x01(\x0b\x32..bilibili.app.viewunite.v1.BizReserveGameParam\"\x91\x01\n\x14OperationCardContent\x12\r\n\x05title\x18\x01 \x01(\t\x12\x10\n\x08subtitle\x18\x02 \x01(\t\x12\x0c\n\x04icon\x18\x03 \x01(\t\x12\x14\n\x0c\x62utton_title\x18\x04 \x01(\t\x12\x1d\n\x15\x62utton_selected_title\x18\x05 \x01(\t\x12\x15\n\rshow_selected\x18\x06 \x01(\x08\"\\\n\x0cPlayStrategy\x12\x12\n\nstrategies\x18\x01 \x03(\t\x12\x1f\n\x17recommend_show_strategy\x18\x02 \x01(\x05\x12\x17\n\x0f\x61uto_play_toast\x18\x03 \x01(\t\"`\n\rPointMaterial\x12\x0b\n\x03url\x18\x01 \x01(\t\x12\x42\n\x0fmaterial_source\x18\x02 \x01(\x0e\x32).bilibili.app.viewunite.v1.MaterialSource\"\xca\x01\n\tSelection\x12\r\n\x05title\x18\x01 \x01(\t\x12\x36\n\x04item\x18\x02 \x03(\x0b\x32(.bilibili.app.viewunite.v1.SelectionItem\x12\x34\n\x08\x61rc_type\x18\x03 \x01(\x0e\x32\".bilibili.app.viewunite.v1.ArcType\x12@\n\x0eselection_type\x18\x04 \x01(\x0e\x32(.bilibili.app.viewunite.v1.SelectionType\"\xbf\x01\n\rSelectionItem\x12\x0b\n\x03\x61id\x18\x01 \x01(\x04\x12\x0b\n\x03\x63id\x18\x02 \x01(\x04\x12\x38\n\nbadge_type\x18\x04 \x01(\x0b\x32$.bilibili.app.viewunite.v1.BadgeType\x12\r\n\x05title\x18\x05 \x01(\t\x12\x12\n\nlong_title\x18\x06 \x01(\t\x12\x37\n\tdimension\x18\x07 \x01(\x0b\x32$.bilibili.app.viewunite.v1.Dimension\"\xca\x01\n\x0fSelectionModule\x12\x37\n\tselection\x18\x01 \x03(\x0b\x32$.bilibili.app.viewunite.v1.Selection\x12>\n\rserial_season\x18\x02 \x03(\x0b\x32\'.bilibili.app.viewunite.v1.SerialSeason\x12>\n\rplay_strategy\x18\x03 \x01(\x0b\x32\'.bilibili.app.viewunite.v1.PlayStrategy\"7\n\x0cSerialSeason\x12\x11\n\tseason_id\x18\x01 \x01(\r\x12\x14\n\x0cseason_title\x18\x02 \x01(\t\"N\n\x08ShowTime\x12\x12\n\nstart_time\x18\x01 \x01(\x05\x12\x10\n\x08\x65nd_time\x18\x02 \x01(\x05\x12\r\n\x05pos_x\x18\x03 \x01(\x01\x12\r\n\x05pos_y\x18\x04 \x01(\x01\"t\n\nUpperInfos\x12\x12\n\nfans_count\x18\x01 \x01(\x04\x12 \n\x18\x61rc_count_last_half_year\x18\x02 \x01(\x04\x12\x16\n\x0e\x66irst_up_dates\x18\x03 \x01(\x03\x12\x18\n\x10total_play_count\x18\x04 \x01(\x04\"\xc3\x01\n\nVideoGuide\x12\x35\n\x08material\x18\x01 \x03(\x0b\x32#.bilibili.app.viewunite.v1.Material\x12>\n\x0bvideo_point\x18\x02 \x01(\x0b\x32).bilibili.app.viewunite.v1.VideoViewPoint\x12>\n\rcontract_card\x18\x03 \x01(\x0b\x32\'.bilibili.app.viewunite.v1.ContractCard\"f\n\nVideoPoint\x12\x0c\n\x04type\x18\x01 \x01(\x05\x12\x0c\n\x04\x66rom\x18\x02 \x01(\x03\x12\n\n\x02to\x18\x03 \x01(\x03\x12\x0f\n\x07\x63ontent\x18\x04 \x01(\t\x12\r\n\x05\x63over\x18\x05 \x01(\t\x12\x10\n\x08logo_url\x18\x06 \x01(\t\"y\n\tVideoShot\x12\x0f\n\x07pv_data\x18\x01 \x01(\t\x12\x11\n\timg_x_len\x18\x02 \x01(\x05\x12\x12\n\nimd_x_size\x18\x03 \x01(\x05\x12\x11\n\timg_y_len\x18\x04 \x01(\x05\x12\x12\n\nimg_y_size\x18\x05 \x01(\x05\x12\r\n\x05image\x18\x06 \x03(\t\"\xa2\x01\n\x0eVideoViewPoint\x12\x35\n\x06points\x18\x01 \x03(\x0b\x32%.bilibili.app.viewunite.v1.VideoPoint\x12@\n\x0epoint_material\x18\x02 \x01(\x0b\x32(.bilibili.app.viewunite.v1.PointMaterial\x12\x17\n\x0fpoint_permanent\x18\x03 \x01(\x08\"|\n\x08ViewBase\x12\x38\n\nunion_type\x18\x01 \x01(\x0e\x32$.bilibili.app.viewunite.v1.UnionType\x12\x36\n\tpage_type\x18\x02 \x01(\x0e\x32#.bilibili.app.viewunite.v1.PageType\"\xaf\x01\n\x0fViewProgressReq\x12\x0b\n\x03\x61id\x18\x01 \x01(\x04\x12\x0b\n\x03\x63id\x18\x02 \x01(\x04\x12\x0e\n\x06up_mid\x18\x03 \x01(\x04\x12>\n\rchronos_param\x18\x04 \x01(\x0b\x32\'.bilibili.app.viewunite.v1.ChronosParam\x12\x32\n\x04type\x18\x05 \x01(\x0e\x32$.bilibili.app.viewunite.v1.UnionType\"\xef\x01\n\x11ViewProgressReply\x12:\n\x0bvideo_guide\x18\x01 \x01(\x0b\x32%.bilibili.app.viewunite.v1.VideoGuide\x12\x33\n\x07\x63hronos\x18\x02 \x01(\x0b\x32\".bilibili.app.viewunite.v1.Chronos\x12\x36\n\x08\x61rc_shot\x18\x03 \x01(\x0b\x32$.bilibili.app.viewunite.v1.VideoShot\x12\x31\n\x02\x64m\x18\x04 \x01(\x0b\x32%.bilibili.app.viewunite.v1.DmResource\"\xc2\x02\n\x07ViewReq\x12\x0b\n\x03\x61id\x18\x01 \x01(\x04\x12\x0c\n\x04\x62vid\x18\x02 \x01(\t\x12\x0c\n\x04\x66rom\x18\x03 \x01(\t\x12\r\n\x05spmid\x18\x04 \x01(\t\x12\x12\n\nfrom_spmid\x18\x05 \x01(\t\x12\x12\n\nsession_id\x18\x06 \x01(\t\x12\x43\n\x0bplayer_args\x18\x07 \x01(\x0b\x32..bilibili.app.archive.middleware.v1.PlayerArgs\x12\x10\n\x08track_id\x18\x08 \x01(\t\x12K\n\rextra_content\x18\t \x03(\x0b\x32\x34.bilibili.app.viewunite.v1.ViewReq.ExtraContentEntry\x1a\x33\n\x11\x45xtraContentEntry\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\t:\x02\x38\x01\"\xb3\x01\n\tViewReply\x12\x36\n\tview_base\x18\x01 \x01(\x0b\x32#.bilibili.app.viewunite.v1.ViewBase\x12\x44\n\x10selection_module\x18\x03 \x01(\x0b\x32*.bilibili.app.viewunite.v1.SelectionModule\x12(\n\nsupplement\x18\x04 \x01(\x0b\x32\x14.google.protobuf.Any*^\n\x07\x41rcType\x12\x0b\n\x07UNKNOWN\x10\x00\x12\t\n\x05PAGES\x10\x01\x12\n\n\x06SERIES\x10\x02\x12\x0c\n\x08POSITIVE\x10\x03\x12\x0b\n\x07SECTION\x10\x04\x12\n\n\x06RELATE\x10\x05\x12\x08\n\x04PUGV\x10\x06*\x91\x01\n\x07\x42izType\x12\x0f\n\x0b\x42izTypeNone\x10\x00\x12\x16\n\x12\x42izTypeFollowVideo\x10\x01\x12\x1a\n\x16\x42izTypeReserveActivity\x10\x02\x12\x13\n\x0f\x42izTypeJumpLink\x10\x03\x12\x14\n\x10\x42izTypeFavSeason\x10\x04\x12\x16\n\x12\x42izTypeReserveGame\x10\x05*\x82\x01\n\x0fMaterialBizType\x12\x08\n\x04NONE\x10\x00\x12\x0c\n\x08\x41\x43TIVITY\x10\x01\x12\x07\n\x03\x42GM\x10\x02\x12\n\n\x06\x45\x46\x46\x45\x43T\x10\x03\x12\x0e\n\nSHOOT_SAME\x10\x04\x12\x12\n\x0eSHOOT_TOGETHER\x10\x05\x12\x11\n\rACTIVITY_ICON\x10\x06\x12\x0b\n\x07NEW_BGM\x10\x07*)\n\x0eMaterialSource\x12\x0b\n\x07\x44\x45\x46\x41ULT\x10\x00\x12\n\n\x06\x42IJIAN\x10\x01*2\n\x0cPageCategory\x12\x0f\n\x0b\x43OMMON_PAGE\x10\x00\x12\x11\n\rACTIVITY_PAGE\x10\x01*\x1a\n\x08PageType\x12\x06\n\x02H5\x10\x00\x12\x06\n\x02NA\x10\x01*.\n\rSelectionType\x12\r\n\tLONGTITLE\x10\x00\x12\x0e\n\nSHORTTITLE\x10\x01*\x1d\n\tUnionType\x12\x07\n\x03UGC\x10\x00\x12\x07\n\x03OGV\x10\x01\x32\xc2\x01\n\x04View\x12P\n\x04View\x12\".bilibili.app.viewunite.v1.ViewReq\x1a$.bilibili.app.viewunite.v1.ViewReply\x12h\n\x0cViewProgress\x12*.bilibili.app.viewunite.v1.ViewProgressReq\x1a,.bilibili.app.viewunite.v1.ViewProgressReplyb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'bilibili.app.viewunite.v1.viewunite_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _VIEWREQ_EXTRACONTENTENTRY._options = None
  _VIEWREQ_EXTRACONTENTENTRY._serialized_options = b'8\001'
  _globals['_ARCTYPE']._serialized_start=5182
  _globals['_ARCTYPE']._serialized_end=5276
  _globals['_BIZTYPE']._serialized_start=5279
  _globals['_BIZTYPE']._serialized_end=5424
  _globals['_MATERIALBIZTYPE']._serialized_start=5427
  _globals['_MATERIALBIZTYPE']._serialized_end=5557
  _globals['_MATERIALSOURCE']._serialized_start=5559
  _globals['_MATERIALSOURCE']._serialized_end=5600
  _globals['_PAGECATEGORY']._serialized_start=5602
  _globals['_PAGECATEGORY']._serialized_end=5652
  _globals['_PAGETYPE']._serialized_start=5654
  _globals['_PAGETYPE']._serialized_end=5680
  _globals['_SELECTIONTYPE']._serialized_start=5682
  _globals['_SELECTIONTYPE']._serialized_end=5728
  _globals['_UNIONTYPE']._serialized_start=5730
  _globals['_UNIONTYPE']._serialized_end=5759
  _globals['_ATTENTIONCARD']._serialized_start=149
  _globals['_ATTENTIONCARD']._serialized_end=220
  _globals['_BADGETYPE']._serialized_start=223
  _globals['_BADGETYPE']._serialized_end=404
  _globals['_BIZFOLLOWVIDEOPARAM']._serialized_start=406
  _globals['_BIZFOLLOWVIDEOPARAM']._serialized_end=446
  _globals['_BIZJUMPLINKPARAM']._serialized_start=448
  _globals['_BIZJUMPLINKPARAM']._serialized_end=479
  _globals['_BIZRESERVEACTIVITYPARAM']._serialized_start=481
  _globals['_BIZRESERVEACTIVITYPARAM']._serialized_end=588
  _globals['_BIZRESERVEGAMEPARAM']._serialized_start=590
  _globals['_BIZRESERVEGAMEPARAM']._serialized_end=628
  _globals['_CHRONOS']._serialized_start=630
  _globals['_CHRONOS']._serialized_end=680
  _globals['_CHRONOSPARAM']._serialized_start=682
  _globals['_CHRONOSPARAM']._serialized_end=767
  _globals['_COMMANDDM']._serialized_start=770
  _globals['_COMMANDDM']._serialized_end=932
  _globals['_CONTRACTCARD']._serialized_start=935
  _globals['_CONTRACTCARD']._serialized_end=1292
  _globals['_CONTRACTTEXT']._serialized_start=1294
  _globals['_CONTRACTTEXT']._serialized_end=1363
  _globals['_DIMENSION']._serialized_start=1365
  _globals['_DIMENSION']._serialized_end=1423
  _globals['_DMRESOURCE']._serialized_start=1426
  _globals['_DMRESOURCE']._serialized_end=1615
  _globals['_MATERIAL']._serialized_start=1618
  _globals['_MATERIAL']._serialized_end=1892
  _globals['_OPERATIONCARD']._serialized_start=1895
  _globals['_OPERATIONCARD']._serialized_end=2338
  _globals['_OPERATIONCARDCONTENT']._serialized_start=2341
  _globals['_OPERATIONCARDCONTENT']._serialized_end=2486
  _globals['_PLAYSTRATEGY']._serialized_start=2488
  _globals['_PLAYSTRATEGY']._serialized_end=2580
  _globals['_POINTMATERIAL']._serialized_start=2582
  _globals['_POINTMATERIAL']._serialized_end=2678
  _globals['_SELECTION']._serialized_start=2681
  _globals['_SELECTION']._serialized_end=2883
  _globals['_SELECTIONITEM']._serialized_start=2886
  _globals['_SELECTIONITEM']._serialized_end=3077
  _globals['_SELECTIONMODULE']._serialized_start=3080
  _globals['_SELECTIONMODULE']._serialized_end=3282
  _globals['_SERIALSEASON']._serialized_start=3284
  _globals['_SERIALSEASON']._serialized_end=3339
  _globals['_SHOWTIME']._serialized_start=3341
  _globals['_SHOWTIME']._serialized_end=3419
  _globals['_UPPERINFOS']._serialized_start=3421
  _globals['_UPPERINFOS']._serialized_end=3537
  _globals['_VIDEOGUIDE']._serialized_start=3540
  _globals['_VIDEOGUIDE']._serialized_end=3735
  _globals['_VIDEOPOINT']._serialized_start=3737
  _globals['_VIDEOPOINT']._serialized_end=3839
  _globals['_VIDEOSHOT']._serialized_start=3841
  _globals['_VIDEOSHOT']._serialized_end=3962
  _globals['_VIDEOVIEWPOINT']._serialized_start=3965
  _globals['_VIDEOVIEWPOINT']._serialized_end=4127
  _globals['_VIEWBASE']._serialized_start=4129
  _globals['_VIEWBASE']._serialized_end=4253
  _globals['_VIEWPROGRESSREQ']._serialized_start=4256
  _globals['_VIEWPROGRESSREQ']._serialized_end=4431
  _globals['_VIEWPROGRESSREPLY']._serialized_start=4434
  _globals['_VIEWPROGRESSREPLY']._serialized_end=4673
  _globals['_VIEWREQ']._serialized_start=4676
  _globals['_VIEWREQ']._serialized_end=4998
  _globals['_VIEWREQ_EXTRACONTENTENTRY']._serialized_start=4947
  _globals['_VIEWREQ_EXTRACONTENTENTRY']._serialized_end=4998
  _globals['_VIEWREPLY']._serialized_start=5001
  _globals['_VIEWREPLY']._serialized_end=5180
  _globals['_VIEW']._serialized_start=5762
  _globals['_VIEW']._serialized_end=5956
# @@protoc_insertion_point(module_scope)
