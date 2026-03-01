def upload_tiktok(
    video: str,
    description: str,
    accountname: str,
    hashtags=None,
    sound_name=None,
    sound_aud_vol: str = "mix",
    schedule=None,
    day=None,
    copyrightcheck: bool = False,
    suppressprint: bool = False,
    headless: bool = True,
    stealth: bool = False,
    proxy=None,
    search_mode: str = "search",
) -> str:
    """
    UPLOADS VIDEO TO TIKTOK (powered by Phantomwright for bot-detection evasion)
    --------------------------------------------------------------------------------
    video (str) -> path to video to upload
    description (str) -> description for video
    accountname (str) -> account to upload on
    hashtags (str)(array)(opt) -> hashtags for video
    sound_name (str)(opt) -> name of tik tok sound to use for video
    sound_aud_vol (str)(opt) -> volume of tik tok sound, 'main', 'mix' or 'background'
    schedule (str)(opt) -> format HH:MM, your local time to upload video
    day (int)(opt) -> day to schedule video for
    copyrightcheck (bool)(opt) -> include copyright check or not
    suppressprint (bool)(opt) -> True means function doesnt print anything
    headless (bool)(opt) -> run in headless mode or not
    stealth (bool)(opt) -> will wait second(s) before each operation
    proxy (dict)(opt) -> proxy server to run code on
    search_mode (str)(opt) -> 'search' or 'favorites'
    """
    try:
        check_for_updates()
    except Exception:
        time.sleep(0.1)

    try:
        validate_proxy(proxy)
    except Exception as e:
        sys.exit(f"Error validating proxy: {e}")

    if accountname is None:
        sys.exit("PLEASE ENTER NAME OF ACCOUNT TO POST ON, READ DOCUMENTATION FOR MORE INFO")

    cookies = _load_or_create_cookies(accountname, proxy)

    with sync_playwright() as p:
        _, context = _make_stealth_context(p, headless=headless, proxy=proxy)
        context.add_cookies(cookies)
        page = context.new_page()

        sim = SyncUserSimulator(page)

        if not suppressprint:
            print(f"Uploading to account '{accountname}'")

        _goto_with_retry(page, UPLOAD_URL)
        sim.simulate_browsing(duration_ms=1500)

        captcha = _wait_for_upload_or_captcha(page)
        if captcha:
            _solve_captcha_if_needed(page, suppressprint)

        _set_video_input(page, video)
        _add_description_and_hashtags(page, sim, video, description, hashtags, stealth, suppressprint)
        _wait_for_upload_ready(page)

        time.sleep(0.2)
        if not suppressprint:
            print("Tik tok done loading file onto servers")

        sim.simulate_browsing(duration_ms=1000)

        schedule, day = _normalize_schedule_and_day(schedule, day)
        _validate_schedule_request(schedule, day)
        _apply_schedule(page, schedule, day, stealth, suppressprint)

        sound_fail = _add_sound_from_upload_page(
            page,
            sound_name,
            sound_aud_vol,
            sim,
            stealth,
            suppressprint,
            search_mode,
        )

        if not sound_fail:
            page.wait_for_selector('div[data-contents="true"]')

            if copyrightcheck:
                _run_upload_copyright_check(page, stealth, suppressprint)

            result = _submit_upload(
                page,
                schedule,
                stealth,
                suppressprint,
                post_success_wait=0.1,
                schedule_success_wait=0.2,
            )
            if result == "Error":
                return "Error"
        else:
            try:
                if stealth:
                    time.sleep(1)
                page.click('button:has-text("Save draft")', timeout=10000)
                sys.exit("ERROR ADDING SOUND: Video saved as draft, please try again or check documentation for more info")
                return "Error"
            except Exception:
                sys.exit("ERROR ADDING SOUND; SAVE AS DRAFT BUTTON NOT FOUND SO VIDEO NOT ADDED AS DRAFT")
                return "Error"


    return "Completed"

