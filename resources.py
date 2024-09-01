'''
module containing dictionaries for various functions of isabelle.
includes tiktok speaker names, as well as strings for responses.
'''

# speaker names used for requests to the tiktok api
# in the format of: friendly name, voice code
speakers = {
    'Ghost Face': 'en_us_ghostface',
    'Chewbacca': 'en_us_chewbacca',
    'C3PO': 'en_us_c3po',
    'Stitch': 'en_us_stitch',
    'Stormtrooper': 'en_us_stormtrooper',
    'Rocket': 'en_us_rocket',
    'Madame Leota': 'en_female_madam_leota',
    'Ghost Host': 'en_male_ghosthost',
    'Pirate': 'en_male_pirate',
    'English AU - Female': 'en_au_001',
    'English AU - Male': 'en_au_002',
    'English UK - Male 1': 'en_uk_001',
    'English UK - Male 2': 'en_uk_003',
    'English US - Female 1': 'en_us_001',
    'English US - Female 2': 'en_us_002',
    'English US - Male 1': 'en_us_006',
    'English US - Male 2': 'en_us_007',
    'English US - Male 3': 'en_us_009',
    'English US - Male 4': 'en_us_010',
    'Narrator': 'en_male_narration',
    'Wacky': 'en_male_funny',
    'Peaceful': 'en_female_emotional',
    'Serious': 'en_male_cody',
    'French - Male 1': 'fr_001',
    'French - Male 2': 'fr_002',
    'German - Female': 'de_001',
    'German - Male': 'de_002',
    'Spanish - Male': 'es_002',
    'Spanish MX - Male': 'es_mx_002',
    'Portuguese BR - Female 1': 'br_001',
    'Portuguese BR - Female 2': 'br_003',
    'Portuguese BR - Female 3': 'br_004',
    'Portuguese BR - Male': 'br_005',
    'Indonesian - Female': 'id_001',
    'Japanese - Female 1': 'jp_001',
    'Japanese - Female 2': 'jp_003',
    'Japanese - Female 3': 'jp_005',
    'Japanese - Male': 'jp_006',
    'Korean - Male 1': 'kr_002',
    'Korean - Female': 'kr_003',
    'Korean - Male 2': 'kr_004',
    'Alto': 'en_female_f08_salut_damour',
    'Tenor': 'en_male_m03_lobby',
    'Sunshine Soon': 'en_male_m03_sunshine_soon',
    'Warmy Breeze': 'en_female_f08_warmy_breeze',
    'Glorious': 'en_female_ht_f08_glorious',
    'It Goes Up': 'en_male_sing_funny_it_goes_up',
    'Chipmunk': 'en_male_m2_xhxs_m03_silly',
    'Dramatic': 'en_female_ht_f08_wonderful_world'
}

# strings used for responses to the user
messages = {
    'desc_listen': 'Repeat anything you say in the current channel.',
    'desc_dismiss': 'Cancel /listen.',
    'desc_shush': 'Interrupt the current voice message.',
    'desc_list': 'Direct message you with a list of speakers.',
    'desc_say': 'Say one thing in the current voice call.',
    'desc_tts': 'Create a .MP3 file.',
    'desc_opt_script': 'The text to say.',
    'desc_opt_speaker': 'The voice to use.',
    'desc_opt_hide': 'Whether to hide the output',
    'rsp_listen': "I'll repeat anything you say in {} using `{}` as a voice.\n(Type /dismiss for me to stop.)",
    'rsp_dismiss': "I'll stop repeating  you.", 'rsp_shush': '{} interrupted the current message.',
    'rsp_connect': "I'm connecting to {}...", 'rsp_list': "I've sent you a list in DMs.",
    'err_no_channel': 'You need to be in a voice channel...',
    'err_diff_channel': "I'm already in {}...",
    'err_not_listening': "I wasn't copying you.",
    'err_char_cap': 'Your message is too long! ({} Characters.)\nThe TikTok API blocks requests over 200 characters.'
}