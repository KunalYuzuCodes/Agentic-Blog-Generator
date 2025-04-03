<!DOCTYPE html><html lang="en" class="js-focus-visible js" data-js-focus-visible=""><head>
    
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width,initial-scale=1">
      
        <meta name="description" content="Agent Framework / shim to use Pydantic with LLMs">
      
      
      
        <link rel="canonical" href="https://ai.pydantic.dev/models/">
      
      
        <link rel="prev" href="../agents/">
      
      
        <link rel="next" href="../dependencies/">
      
      
      <link rel="icon" href="../favicon.ico">
      <meta name="generator" content="mkdocs-1.6.1, mkdocs-material-9.6.5">
    
    
      
        <title>Models - PydanticAI</title>
      
    
    
      <link rel="stylesheet" href="../assets/stylesheets/main.8608ea7d.min.css">
      
        
        <link rel="stylesheet" href="../assets/stylesheets/palette.06af60db.min.css">
      
      


    
    
      
    
    
      
        
        
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300i,400,400i,700,700i%7CRoboto+Mono:400,400i,700,700i&amp;display=fallback">
        <style>:root{--md-text-font:"Roboto";--md-code-font:"Roboto Mono"}</style>
      
    
    
      <link rel="stylesheet" href="../assets/_mkdocstrings.css">
    
      <link rel="stylesheet" href="../extra/tweaks.css">
    
    <script>__md_scope=new URL("..",location),__md_hash=e=>[...e].reduce(((e,_)=>(e<<5)-e+_.charCodeAt(0)),0),__md_get=(e,_=localStorage,t=__md_scope)=>JSON.parse(_.getItem(t.pathname+"."+e)),__md_set=(e,_,t=localStorage,a=__md_scope)=>{try{t.setItem(a.pathname+"."+e,JSON.stringify(_))}catch(e){}}</script>
    
      

    
    
      
        <meta property="og:type" content="website">
      
        <meta property="og:title" content="Models - PydanticAI">
      
        <meta property="og:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta property="og:image" content="https://ai.pydantic.dev/assets/images/social/models.png">
      
        <meta property="og:image:type" content="image/png">
      
        <meta property="og:image:width" content="1200">
      
        <meta property="og:image:height" content="630">
      
        <meta property="og:url" content="https://ai.pydantic.dev/models/">
      
        <meta name="twitter:card" content="summary_large_image">
      
        <meta name="twitter:title" content="Models - PydanticAI">
      
        <meta name="twitter:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta name="twitter:image" content="https://ai.pydantic.dev/assets/images/social/models.png">
      
    
    
   <link href="../assets/stylesheets/glightbox.min.css" rel="stylesheet"><style>
    html.glightbox-open { overflow: initial; height: 100%; }
    .gslide-title { margin-top: 0px; user-select: text; }
    .gslide-desc { color: #666; user-select: text; }
    .gslide-image img { background: white; }
    .gscrollbar-fixer { padding-right: 15px; }
    .gdesc-inner { font-size: 0.75rem; }
    body[data-md-color-scheme="slate"] .gdesc-inner { background: var(--md-default-bg-color);}
    body[data-md-color-scheme="slate"] .gslide-title { color: var(--md-default-fg-color);}
    body[data-md-color-scheme="slate"] .gslide-desc { color: var(--md-default-fg-color);}</style> <script src="../assets/javascripts/glightbox.min.js"></script><meta name="theme-color" content="#e92063"><meta name="color-scheme" content="light"></head>
  
  
    
    
      
    
    
    
    
    <body dir="ltr" data-md-color-scheme="default" data-md-color-primary="pink" data-md-color-accent="pink" data-md-color-media="(prefers-color-scheme)">
  
    
    <input class="md-toggle" data-md-toggle="drawer" type="checkbox" id="__drawer" autocomplete="off">
    <input class="md-toggle" data-md-toggle="search" type="checkbox" id="__search" autocomplete="off">
    <label class="md-overlay" for="__drawer"></label>
    <div data-md-component="skip">
      
        
        <a href="#models-interfaces-and-providers" class="md-skip">
          Skip to content
        </a>
      
    </div>
    <div data-md-component="announce">
      
    </div>
    
    
      

  

<header class="md-header md-header--shadow" data-md-component="header">
  <nav class="md-header__inner md-grid" aria-label="Header">
    <a href=".." title="PydanticAI" class="md-header__button md-logo" aria-label="PydanticAI" data-md-component="logo">
      
  <img src="../img/logo-white.svg" alt="logo">

    </a>
    <label class="md-header__button md-icon" for="__drawer">
      
      <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M3 6h18v2H3zm0 5h18v2H3zm0 5h18v2H3z"></path></svg>
    </label>
    <div class="md-header__title" data-md-component="header-title">
      <div class="md-header__ellipsis">
        <div class="md-header__topic">
          <span class="md-ellipsis">
            PydanticAI
          </span>
        </div>
        <div class="md-header__topic" data-md-component="header-topic">
          <span class="md-ellipsis">
            
              Models
            
          </span>
        </div>
      </div>
    </div>
    
      
        <form class="md-header__option" data-md-component="palette">
  
    
    
    
    <input class="md-option" data-md-color-media="(prefers-color-scheme)" data-md-color-scheme="default" data-md-color-primary="pink" data-md-color-accent="pink" aria-label="Switch to light mode" type="radio" name="__palette" id="__palette_0">
    
      <label class="md-header__button md-icon" title="Switch to light mode" for="__palette_1">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2a7 7 0 0 0-7 7c0 2.38 1.19 4.47 3 5.74V17a1 1 0 0 0 1 1h6a1 1 0 0 0 1-1v-2.26c1.81-1.27 3-3.36 3-5.74a7 7 0 0 0-7-7M9 21a1 1 0 0 0 1 1h4a1 1 0 0 0 1-1v-1H9z"></path></svg>
      </label>
    
  
    
    
    
    <input class="md-option" data-md-color-media="(prefers-color-scheme: light)" data-md-color-scheme="default" data-md-color-primary="pink" data-md-color-accent="pink" aria-label="Switch to dark mode" type="radio" name="__palette" id="__palette_1">
    
      <label class="md-header__button md-icon" title="Switch to dark mode" for="__palette_2" hidden="">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M12 2a7 7 0 0 1 7 7c0 2.38-1.19 4.47-3 5.74V17a1 1 0 0 1-1 1H9a1 1 0 0 1-1-1v-2.26C6.19 13.47 5 11.38 5 9a7 7 0 0 1 7-7M9 21v-1h6v1a1 1 0 0 1-1 1h-4a1 1 0 0 1-1-1m3-17a5 5 0 0 0-5 5c0 2.05 1.23 3.81 3 4.58V16h4v-2.42c1.77-.77 3-2.53 3-4.58a5 5 0 0 0-5-5"></path></svg>
      </label>
    
  
    
    
    
    <input class="md-option" data-md-color-media="(prefers-color-scheme: dark)" data-md-color-scheme="slate" data-md-color-primary="pink" data-md-color-accent="pink" aria-label="Switch to system preference" type="radio" name="__palette" id="__palette_2">
    
      <label class="md-header__button md-icon" title="Switch to system preference" for="__palette_0" hidden="">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9 2c3.87 0 7 3.13 7 7 0 2.38-1.19 4.47-3 5.74V17c0 .55-.45 1-1 1H6c-.55 0-1-.45-1-1v-2.26C3.19 13.47 2 11.38 2 9c0-3.87 3.13-7 7-7M6 21v-1h6v1c0 .55-.45 1-1 1H7c-.55 0-1-.45-1-1M9 4C6.24 4 4 6.24 4 9c0 2.05 1.23 3.81 3 4.58V16h4v-2.42c1.77-.77 3-2.53 3-4.58 0-2.76-2.24-5-5-5m10 9h-2l-3.2 9h1.9l.7-2h3.2l.7 2h1.9zm-2.15 5.65L18 15l1.15 3.65z"></path></svg>
      </label>
    
  
</form>
      
    
    
      <script>var palette=__md_get("__palette");if(palette&&palette.color){if("(prefers-color-scheme)"===palette.color.media){var media=matchMedia("(prefers-color-scheme: light)"),input=document.querySelector(media.matches?"[data-md-color-media='(prefers-color-scheme: light)']":"[data-md-color-media='(prefers-color-scheme: dark)']");palette.color.media=input.getAttribute("data-md-color-media"),palette.color.scheme=input.getAttribute("data-md-color-scheme"),palette.color.primary=input.getAttribute("data-md-color-primary"),palette.color.accent=input.getAttribute("data-md-color-accent")}for(var[key,value]of Object.entries(palette.color))document.body.setAttribute("data-md-color-"+key,value)}</script>
    
    
    
      <label class="md-header__button md-icon" for="__search">
        
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9.5 3A6.5 6.5 0 0 1 16 9.5c0 1.61-.59 3.09-1.56 4.23l.27.27h.79l5 5-1.5 1.5-5-5v-.79l-.27-.27A6.52 6.52 0 0 1 9.5 16 6.5 6.5 0 0 1 3 9.5 6.5 6.5 0 0 1 9.5 3m0 2C7 5 5 7 5 9.5S7 14 9.5 14 14 12 14 9.5 12 5 9.5 5"></path></svg>
      </label>
      <div class="md-search" role="dialog">
  <label class="md-search__overlay" for="__search"></label>
  <div class="md-search__inner" role="search">
    <form class="md-search__form" name="search">
      <input type="text" id="searchbox" class="md-search__input" name="query" aria-label="Search" placeholder="Search" autocapitalize="off" autocorrect="off" autocomplete="off" spellcheck="false" required="">
      <label class="md-search__icon md-icon" for="__search">

        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M9.5 3A6.5 6.5 0 0 1 16 9.5c0 1.61-.59 3.09-1.56 4.23l.27.27h.79l5 5-1.5 1.5-5-5v-.79l-.27-.27A6.516 6.516 0 0 1 9.5 16 6.5 6.5 0 0 1 3 9.5 6.5 6.5 0 0 1 9.5 3m0 2C7 5 5 7 5 9.5S7 14 9.5 14 14 12 14 9.5 12 5 9.5 5Z"></path></svg>

        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M20 11v2H8l5.5 5.5-1.42 1.42L4.16 12l7.92-7.92L13.5 5.5 8 11h12Z"></path></svg>
      </label>
      <nav class="md-search__options" aria-label="Search">

        <button id="searchbox-clear" type="reset" class="md-search__icon md-icon" title="Clear" aria-label="Clear" tabindex="-1">

          <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><path d="M19 6.41 17.59 5 12 10.59 6.41 5 5 6.41 10.59 12 5 17.59 6.41 19 12 13.41 17.59 19 19 17.59 13.41 12 19 6.41Z"></path></svg>
        </button>
      </nav>

        <div class="md-search__suggest"></div>

    </form>
    <div class="md-search__output">
      <div class="md-search__scrollwrap" tabindex="0">
        <div class="md-search-result">
          <div class="md-search-result__meta" id="type-to-start-searching">Type to start searching</div>
          <ol class="md-search-result__list" id="hits" role="presentation" hidden=""></ol>
        </div>
      </div>
    </div>
  </div>
</div>
    
    
      <div class="md-header__source">
        <a href="https://github.com/pydantic/pydantic-ai" title="Go to repository" class="md-source" data-md-component="source">
  <div class="md-source__icon md-icon">
    
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!--! Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2024 Fonticons, Inc.--><path d="M439.55 236.05 244 40.45a28.87 28.87 0 0 0-40.81 0l-40.66 40.63 51.52 51.52c27.06-9.14 52.68 16.77 43.39 43.68l49.66 49.66c34.23-11.8 61.18 31 35.47 56.69-26.49 26.49-70.21-2.87-56-37.34L240.22 199v121.85c25.3 12.54 22.26 41.85 9.08 55a34.34 34.34 0 0 1-48.55 0c-17.57-17.6-11.07-46.91 11.25-56v-123c-20.8-8.51-24.6-30.74-18.64-45L142.57 101 8.45 235.14a28.86 28.86 0 0 0 0 40.81l195.61 195.6a28.86 28.86 0 0 0 40.8 0l194.69-194.69a28.86 28.86 0 0 0 0-40.81"></path></svg>
  </div>
  <div class="md-source__repository md-source__repository--active">
    pydantic/pydantic-ai
  <ul class="md-source__facts"><li class="md-source__fact md-source__fact--version">v0.0.50</li><li class="md-source__fact md-source__fact--stars">8k</li><li class="md-source__fact md-source__fact--forks">687</li></ul></div>
</a>
      </div>
    
  </nav>
  
</header>
    
    <div class="md-container" data-md-component="container">
      
      
        
          
        
      
      <main class="md-main" data-md-component="main">
        <div class="md-main__inner md-grid">
          
            
              
              <div class="md-sidebar md-sidebar--primary" data-md-component="sidebar" data-md-type="navigation">
                <div class="md-sidebar__scrollwrap">
                  <div class="md-sidebar__inner">
                    



<nav class="md-nav md-nav--primary" aria-label="Navigation" data-md-level="0">
  <label class="md-nav__title" for="__drawer">
    <a href=".." title="PydanticAI" class="md-nav__button md-logo" aria-label="PydanticAI" data-md-component="logo">
      
  <img src="../img/logo-white.svg" alt="logo">

    </a>
    PydanticAI
  </label>
  
    <div class="md-nav__source">
      <a href="https://github.com/pydantic/pydantic-ai" title="Go to repository" class="md-source" data-md-component="source">
  <div class="md-source__icon md-icon">
    
    <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512"><!--! Font Awesome Free 6.7.2 by @fontawesome - https://fontawesome.com License - https://fontawesome.com/license/free (Icons: CC BY 4.0, Fonts: SIL OFL 1.1, Code: MIT License) Copyright 2024 Fonticons, Inc.--><path d="M439.55 236.05 244 40.45a28.87 28.87 0 0 0-40.81 0l-40.66 40.63 51.52 51.52c27.06-9.14 52.68 16.77 43.39 43.68l49.66 49.66c34.23-11.8 61.18 31 35.47 56.69-26.49 26.49-70.21-2.87-56-37.34L240.22 199v121.85c25.3 12.54 22.26 41.85 9.08 55a34.34 34.34 0 0 1-48.55 0c-17.57-17.6-11.07-46.91 11.25-56v-123c-20.8-8.51-24.6-30.74-18.64-45L142.57 101 8.45 235.14a28.86 28.86 0 0 0 0 40.81l195.61 195.6a28.86 28.86 0 0 0 40.8 0l194.69-194.69a28.86 28.86 0 0 0 0-40.81"></path></svg>
  </div>
  <div class="md-source__repository md-source__repository--active">
    pydantic/pydantic-ai
  <ul class="md-source__facts"><li class="md-source__fact md-source__fact--version">v0.0.50</li><li class="md-source__fact md-source__fact--stars">8k</li><li class="md-source__fact md-source__fact--forks">687</li></ul></div>
</a>
    </div>
  
  <ul class="md-nav__list">
    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href=".." class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Introduction
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../install/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Installation
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../help/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Getting Help
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../contributing/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Contributing
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../troubleshooting/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Troubleshooting
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
    
  
  
  
    
    
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
      
        
        
      
    
    
    <li class="md-nav__item md-nav__item--active md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_6" checked="">
        
          
          <label class="md-nav__link" for="__nav_6" id="__nav_6_label" tabindex="">
            
  
  <span class="md-ellipsis">
    Documentation
    
  </span>
  

            <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_6_label" aria-expanded="true">
          <label class="md-nav__title" for="__nav_6">
            <span class="md-nav__icon md-icon"></span>
            Documentation
          </label>
          <ul class="md-nav__list">
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../agents/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Agents
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
    
  
  
  
    <li class="md-nav__item md-nav__item--active">
      
      <input class="md-nav__toggle md-toggle" type="checkbox" id="__toc">
      
      
      
        <label class="md-nav__link md-nav__link--active" for="__toc">
          
  
  <span class="md-ellipsis">
    Models
    
  </span>
  

          <span class="md-nav__icon md-icon"></span>
        </label>
      
      <a href="./" class="md-nav__link md-nav__link--active">
        
  
  <span class="md-ellipsis">
    Models
    
  </span>
  

      </a>
      
        

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
  
    <label class="md-nav__title" for="__toc">
      <span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
    <ul class="md-nav__list" data-md-component="toc">
      
        <li class="md-nav__item">
  <a href="#models-interfaces-and-providers" class="md-nav__link">
    <span class="md-ellipsis">
      Models, Interfaces, and Providers
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#openai" class="md-nav__link">
    <span class="md-ellipsis">
      OpenAI
    </span>
  </a>
  
    <nav class="md-nav" aria-label="OpenAI">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#install" class="md-nav__link">
    <span class="md-ellipsis">
      Install
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#configuration" class="md-nav__link">
    <span class="md-ellipsis">
      Configuration
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#environment-variable" class="md-nav__link">
    <span class="md-ellipsis">
      Environment variable
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#provider-argument" class="md-nav__link">
    <span class="md-ellipsis">
      provider argument
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#custom-openai-client" class="md-nav__link">
    <span class="md-ellipsis">
      Custom OpenAI Client
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#openai-responses-api" class="md-nav__link">
    <span class="md-ellipsis">
      OpenAI Responses API
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#anthropic" class="md-nav__link">
    <span class="md-ellipsis">
      Anthropic
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Anthropic">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#install_1" class="md-nav__link">
    <span class="md-ellipsis">
      Install
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#configuration_1" class="md-nav__link">
    <span class="md-ellipsis">
      Configuration
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#environment-variable_1" class="md-nav__link">
    <span class="md-ellipsis">
      Environment variable
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#provider-argument_1" class="md-nav__link">
    <span class="md-ellipsis">
      provider argument
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#custom-http-client" class="md-nav__link">
    <span class="md-ellipsis">
      Custom HTTP Client
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#gemini" class="md-nav__link">
    <span class="md-ellipsis">
      Gemini
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Gemini">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#install_2" class="md-nav__link">
    <span class="md-ellipsis">
      Install
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#configuration_2" class="md-nav__link">
    <span class="md-ellipsis">
      Configuration
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#environment-variable_2" class="md-nav__link">
    <span class="md-ellipsis">
      Environment variable
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#provider-argument_2" class="md-nav__link">
    <span class="md-ellipsis">
      provider argument
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#gemini-via-vertexai" class="md-nav__link">
    <span class="md-ellipsis">
      Gemini via VertexAI
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Gemini via VertexAI">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#install_3" class="md-nav__link">
    <span class="md-ellipsis">
      Install
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#configuration_3" class="md-nav__link">
    <span class="md-ellipsis">
      Configuration
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#application-default-credentials" class="md-nav__link">
    <span class="md-ellipsis">
      Application default credentials
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#service-account" class="md-nav__link">
    <span class="md-ellipsis">
      Service account
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#customising-region" class="md-nav__link">
    <span class="md-ellipsis">
      Customising region
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#groq" class="md-nav__link">
    <span class="md-ellipsis">
      Groq
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Groq">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#install_4" class="md-nav__link">
    <span class="md-ellipsis">
      Install
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#configuration_4" class="md-nav__link">
    <span class="md-ellipsis">
      Configuration
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#environment-variable_3" class="md-nav__link">
    <span class="md-ellipsis">
      Environment variable
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#provider-argument_3" class="md-nav__link">
    <span class="md-ellipsis">
      provider argument
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#mistral" class="md-nav__link">
    <span class="md-ellipsis">
      Mistral
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Mistral">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#install_5" class="md-nav__link">
    <span class="md-ellipsis">
      Install
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#configuration_5" class="md-nav__link">
    <span class="md-ellipsis">
      Configuration
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#environment-variable_4" class="md-nav__link">
    <span class="md-ellipsis">
      Environment variable
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#provider-argument_4" class="md-nav__link">
    <span class="md-ellipsis">
      provider argument
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#cohere" class="md-nav__link">
    <span class="md-ellipsis">
      Cohere
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Cohere">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#install_6" class="md-nav__link">
    <span class="md-ellipsis">
      Install
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#configuration_6" class="md-nav__link">
    <span class="md-ellipsis">
      Configuration
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#environment-variable_5" class="md-nav__link">
    <span class="md-ellipsis">
      Environment variable
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#provider-argument_5" class="md-nav__link">
    <span class="md-ellipsis">
      provider argument
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#bedrock" class="md-nav__link">
    <span class="md-ellipsis">
      Bedrock
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Bedrock">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#install_7" class="md-nav__link">
    <span class="md-ellipsis">
      Install
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#configuration_7" class="md-nav__link">
    <span class="md-ellipsis">
      Configuration
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#environment-variables" class="md-nav__link">
    <span class="md-ellipsis">
      Environment variables
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#provider-argument_6" class="md-nav__link">
    <span class="md-ellipsis">
      provider argument
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#openai-compatible-models" class="md-nav__link">
    <span class="md-ellipsis">
      OpenAI-compatible Models
    </span>
  </a>
  
    <nav class="md-nav" aria-label="OpenAI-compatible Models">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#ollama" class="md-nav__link">
    <span class="md-ellipsis">
      Ollama
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Ollama">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#example-local-usage" class="md-nav__link">
    <span class="md-ellipsis">
      Example local usage
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#example-using-a-remote-server" class="md-nav__link">
    <span class="md-ellipsis">
      Example using a remote server
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
        
          <li class="md-nav__item">
  <a href="#azure-ai-foundry" class="md-nav__link">
    <span class="md-ellipsis">
      Azure AI Foundry
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#openrouter" class="md-nav__link">
    <span class="md-ellipsis">
      OpenRouter
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#grok-xai" class="md-nav__link">
    <span class="md-ellipsis">
      Grok (xAI)
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#perplexity" class="md-nav__link">
    <span class="md-ellipsis">
      Perplexity
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#fireworks-ai" class="md-nav__link">
    <span class="md-ellipsis">
      Fireworks AI
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#together-ai" class="md-nav__link">
    <span class="md-ellipsis">
      Together AI
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#implementing-custom-models" class="md-nav__link">
    <span class="md-ellipsis">
      Implementing Custom Models
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#fallback" class="md-nav__link">
    <span class="md-ellipsis">
      Fallback
    </span>
  </a>
  
</li>
      
    </ul>
  
</nav>
      
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../dependencies/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Dependencies
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Function Tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../common-tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Common Tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../results/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Results
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../message-history/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Messages and chat history
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../testing/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Unit testing
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../logfire/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Debugging and Monitoring
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../multi-agent-applications/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Multi-agent Applications
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Graphs
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../evals/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Evals
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../input/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Image, Audio &amp; Document Input
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    
    
      
        
          
        
      
        
      
        
      
        
      
    
    
      
    
    
    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_6_14">
        
          
          
          <div class="md-nav__link md-nav__container">
            <a href="../mcp/" class="md-nav__link ">
              
  
  <span class="md-ellipsis">
    MCP
    
  </span>
  

            </a>
            
              
              <label class="md-nav__link " for="__nav_6_14" id="__nav_6_14_label" tabindex="0">
                <span class="md-nav__icon md-icon"></span>
              </label>
            
          </div>
        
        <nav class="md-nav" data-md-level="2" aria-labelledby="__nav_6_14_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_6_14">
            <span class="md-nav__icon md-icon"></span>
            MCP
          </label>
          <ul class="md-nav__list">
            
              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../mcp/client/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Client
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../mcp/server/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Server
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../mcp/run-python/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    MCP Run Python
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../cli/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Command Line Interface (CLI)
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

    
      
      
  
  
  
  
    
    
      
        
          
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
      
        
        
      
    
    
    <li class="md-nav__item md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_7">
        
          
          
          <div class="md-nav__link md-nav__container">
            <a href="../examples/" class="md-nav__link ">
              
  
  <span class="md-ellipsis">
    Examples
    
  </span>
  

            </a>
            
              
              <label class="md-nav__link " for="__nav_7" id="__nav_7_label" tabindex="">
                <span class="md-nav__icon md-icon"></span>
              </label>
            
          </div>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_7_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_7">
            <span class="md-nav__icon md-icon"></span>
            Examples
          </label>
          <ul class="md-nav__list">
            
              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/pydantic-model/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Pydantic Model
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/weather-agent/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Weather agent
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/bank-support/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Bank support
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/sql-gen/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    SQL Generation
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/flight-booking/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Flight booking
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/rag/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    RAG
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/stream-markdown/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Stream markdown
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/stream-whales/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Stream whales
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/chat-app/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Chat App with FastAPI
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../examples/question-graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Question Graph
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

    
      
      
  
  
  
  
    
    
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
      
        
        
      
    
    
    <li class="md-nav__item md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_8">
        
          
          <label class="md-nav__link" for="__nav_8" id="__nav_8_label" tabindex="">
            
  
  <span class="md-ellipsis">
    API Reference
    
  </span>
  

            <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_8_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_8">
            <span class="md-nav__icon md-icon"></span>
            API Reference
          </label>
          <ul class="md-nav__list">
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/agent/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.agent
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/common_tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.common_tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/result/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.result
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/messages/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.messages
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/exceptions/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.exceptions
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/settings/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.settings
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/usage/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.usage
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/mcp/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.mcp
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/format_as_xml/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.format_as_xml
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/base/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/openai/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.openai
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/anthropic/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.anthropic
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/bedrock/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.bedrock
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/cohere/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.cohere
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/gemini/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.gemini
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/groq/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.groq
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/instrumented/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.instrumented
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/mistral/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.mistral
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/test/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.test
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/function/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.function
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/fallback/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.fallback
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/models/wrapper/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.wrapper
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/providers/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.providers
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_graph/graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_graph/nodes/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.nodes
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_graph/persistence/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.persistence
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_graph/mermaid/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.mermaid
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_graph/exceptions/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.exceptions
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_evals/dataset/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.dataset
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_evals/evaluators/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.evaluators
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_evals/reporting/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.reporting
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_evals/otel/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.otel
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../api/pydantic_evals/generation/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.generation
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

    
  </ul>
</nav>
                  </div>
                </div>
              </div>
            
            
              
              <div class="md-sidebar md-sidebar--secondary" data-md-component="sidebar" data-md-type="toc" style="top: 48px;">
                <div class="md-sidebar__scrollwrap" style="height: 474px;">
                  <div class="md-sidebar__inner">
                    

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
  
    <label class="md-nav__title" for="__toc">
      <span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
    <ul class="md-nav__list" data-md-component="toc">
      
        <li class="md-nav__item">
  <a href="#models-interfaces-and-providers" class="md-nav__link">
    <span class="md-ellipsis">
      Models, Interfaces, and Providers
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#openai" class="md-nav__link">
    <span class="md-ellipsis">
      OpenAI
    </span>
  </a>
  
    <nav class="md-nav" aria-label="OpenAI">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#install" class="md-nav__link">
    <span class="md-ellipsis">
      Install
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#configuration" class="md-nav__link">
    <span class="md-ellipsis">
      Configuration
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#environment-variable" class="md-nav__link">
    <span class="md-ellipsis">
      Environment variable
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#provider-argument" class="md-nav__link">
    <span class="md-ellipsis">
      provider argument
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#custom-openai-client" class="md-nav__link">
    <span class="md-ellipsis">
      Custom OpenAI Client
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#openai-responses-api" class="md-nav__link">
    <span class="md-ellipsis">
      OpenAI Responses API
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#anthropic" class="md-nav__link">
    <span class="md-ellipsis">
      Anthropic
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Anthropic">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#install_1" class="md-nav__link">
    <span class="md-ellipsis">
      Install
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#configuration_1" class="md-nav__link">
    <span class="md-ellipsis">
      Configuration
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#environment-variable_1" class="md-nav__link">
    <span class="md-ellipsis">
      Environment variable
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#provider-argument_1" class="md-nav__link">
    <span class="md-ellipsis">
      provider argument
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#custom-http-client" class="md-nav__link">
    <span class="md-ellipsis">
      Custom HTTP Client
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#gemini" class="md-nav__link">
    <span class="md-ellipsis">
      Gemini
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Gemini">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#install_2" class="md-nav__link">
    <span class="md-ellipsis">
      Install
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#configuration_2" class="md-nav__link">
    <span class="md-ellipsis">
      Configuration
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#environment-variable_2" class="md-nav__link">
    <span class="md-ellipsis">
      Environment variable
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#provider-argument_2" class="md-nav__link">
    <span class="md-ellipsis">
      provider argument
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#gemini-via-vertexai" class="md-nav__link">
    <span class="md-ellipsis">
      Gemini via VertexAI
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Gemini via VertexAI">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#install_3" class="md-nav__link">
    <span class="md-ellipsis">
      Install
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#configuration_3" class="md-nav__link">
    <span class="md-ellipsis">
      Configuration
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#application-default-credentials" class="md-nav__link">
    <span class="md-ellipsis">
      Application default credentials
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#service-account" class="md-nav__link">
    <span class="md-ellipsis">
      Service account
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#customising-region" class="md-nav__link">
    <span class="md-ellipsis">
      Customising region
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#groq" class="md-nav__link">
    <span class="md-ellipsis">
      Groq
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Groq">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#install_4" class="md-nav__link">
    <span class="md-ellipsis">
      Install
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#configuration_4" class="md-nav__link">
    <span class="md-ellipsis">
      Configuration
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#environment-variable_3" class="md-nav__link">
    <span class="md-ellipsis">
      Environment variable
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#provider-argument_3" class="md-nav__link">
    <span class="md-ellipsis">
      provider argument
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#mistral" class="md-nav__link">
    <span class="md-ellipsis">
      Mistral
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Mistral">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#install_5" class="md-nav__link">
    <span class="md-ellipsis">
      Install
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#configuration_5" class="md-nav__link">
    <span class="md-ellipsis">
      Configuration
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#environment-variable_4" class="md-nav__link">
    <span class="md-ellipsis">
      Environment variable
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#provider-argument_4" class="md-nav__link">
    <span class="md-ellipsis">
      provider argument
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#cohere" class="md-nav__link">
    <span class="md-ellipsis">
      Cohere
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Cohere">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#install_6" class="md-nav__link">
    <span class="md-ellipsis">
      Install
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#configuration_6" class="md-nav__link">
    <span class="md-ellipsis">
      Configuration
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#environment-variable_5" class="md-nav__link">
    <span class="md-ellipsis">
      Environment variable
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#provider-argument_5" class="md-nav__link">
    <span class="md-ellipsis">
      provider argument
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#bedrock" class="md-nav__link">
    <span class="md-ellipsis">
      Bedrock
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Bedrock">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#install_7" class="md-nav__link">
    <span class="md-ellipsis">
      Install
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#configuration_7" class="md-nav__link">
    <span class="md-ellipsis">
      Configuration
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#environment-variables" class="md-nav__link">
    <span class="md-ellipsis">
      Environment variables
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#provider-argument_6" class="md-nav__link">
    <span class="md-ellipsis">
      provider argument
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#openai-compatible-models" class="md-nav__link">
    <span class="md-ellipsis">
      OpenAI-compatible Models
    </span>
  </a>
  
    <nav class="md-nav" aria-label="OpenAI-compatible Models">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#ollama" class="md-nav__link">
    <span class="md-ellipsis">
      Ollama
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Ollama">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#example-local-usage" class="md-nav__link">
    <span class="md-ellipsis">
      Example local usage
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#example-using-a-remote-server" class="md-nav__link">
    <span class="md-ellipsis">
      Example using a remote server
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
        
          <li class="md-nav__item">
  <a href="#azure-ai-foundry" class="md-nav__link">
    <span class="md-ellipsis">
      Azure AI Foundry
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#openrouter" class="md-nav__link">
    <span class="md-ellipsis">
      OpenRouter
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#grok-xai" class="md-nav__link">
    <span class="md-ellipsis">
      Grok (xAI)
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#perplexity" class="md-nav__link">
    <span class="md-ellipsis">
      Perplexity
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#fireworks-ai" class="md-nav__link">
    <span class="md-ellipsis">
      Fireworks AI
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#together-ai" class="md-nav__link">
    <span class="md-ellipsis">
      Together AI
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#implementing-custom-models" class="md-nav__link">
    <span class="md-ellipsis">
      Implementing Custom Models
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#fallback" class="md-nav__link">
    <span class="md-ellipsis">
      Fallback
    </span>
  </a>
  
</li>
      
    </ul>
  
</nav>
                  </div>
                </div>
              </div>
            
          
          
            <div class="md-content" data-md-component="content">
              <article class="md-content__inner md-typeset">
                
                  


  
  


  <h1>Models</h1>

<p>PydanticAI is Model-agnostic and has built in support for the following model providers:</p>
<ul>
<li><a href="#openai">OpenAI</a></li>
<li><a href="#anthropic">Anthropic</a></li>
<li>Gemini via two different APIs: <a href="#gemini">Generative Language API</a> and <a href="#gemini-via-vertexai">VertexAI API</a></li>
<li><a href="#ollama">Ollama</a></li>
<li><a href="#groq">Groq</a></li>
<li><a href="#mistral">Mistral</a></li>
<li><a href="#cohere">Cohere</a></li>
<li><a href="#bedrock">Bedrock</a></li>
</ul>
<p>See <a href="#openai-compatible-models">OpenAI-compatible models</a> for more examples on how to use models such as <a href="#openrouter">OpenRouter</a>, and <a href="#grok-xai">Grok (xAI)</a> that support the OpenAI SDK.</p>
<p>You can also <a href="#implementing-custom-models">add support for other models</a>.</p>
<p>PydanticAI also comes with <a href="../api/models/test/"><code>TestModel</code></a> and <a href="../api/models/function/"><code>FunctionModel</code></a> for testing and development.</p>
<p>To use each model provider, you need to configure your local environment and make sure you have the right packages installed.</p>
<h2 id="models-interfaces-and-providers">Models, Interfaces, and Providers</h2>
<p>PydanticAI uses a few key terms to describe how it interacts with different LLMs:</p>
<ul>
<li><strong>Model</strong>: This refers to the specific LLM model you want to handle your requests (e.g., <code>gpt-4o</code>, <code>claude-3-5-sonnet-latest</code>,
    <code>gemini-1.5-flash</code>). It's the "brain" that processes your prompts and generates responses.  You specify the
    <em>Model</em> as a parameter to the <em>Interface</em>.</li>
<li><strong>Interface</strong>: This refers to a PydanticAI class used to make requests following a specific LLM API
    (generally by wrapping a vendor-provided SDK, like the <code>openai</code> python SDK). These classes implement a
    vendor-SDK-agnostic API, ensuring a single PydanticAI agent is portable to different LLM vendors without
    any other code changes just by swapping out the <em>Interface</em> it uses. Currently, interface classes are named
    roughly in the format <code>&lt;VendorSdk&gt;Model</code>, for example, we have <code>OpenAIModel</code>, <code>AnthropicModel</code>, <code>GeminiModel</code>,
    etc. These <code>Model</code> classes will soon be renamed to <code>&lt;VendorSdk&gt;Interface</code> to reflect this terminology better.</li>
<li><strong>Provider</strong>: This refers to <em>Interface</em>-specific classes which handle the authentication and connections to an LLM vendor.
    Passing a non-default <em>Provider</em> as a parameter to an <em>Interface</em> is how you can ensure that your agent will make
    requests to a specific endpoint, or make use of a specific approach to authentication (e.g., you can use Vertex-specific
    auth with the <code>GeminiModel</code> by way of the <code>VertexProvider</code>). In particular, this is how you can make use of an AI gateway,
    or an LLM vendor that offers API compatibility with the vendor SDK used by an existing interface (such as <code>OpenAIModel</code>).</li>
</ul>
<p>In short, you select a <em>model</em>, PydanticAI uses the appropriate <em>interface</em> class, and the <em>provider</em> handles the
connection and authentication to the underlying service.</p>
<h2 id="openai">OpenAI</h2>
<h3 id="install">Install</h3>
<p>To use OpenAI models, you need to either install <a href="../install/"><code>pydantic-ai</code></a>, or install <a href="../install/#slim-install"><code>pydantic-ai-slim</code></a> with the <code>openai</code> optional group:</p>
<div class="tabbed-set tabbed-alternate" data-tabs="1:2"><input checked="checked" id="__tabbed_1_1" name="__tabbed_1" type="radio"><input id="__tabbed_1_2" name="__tabbed_1" type="radio"><div class="tabbed-labels tabbed-labels--linked"><label for="__tabbed_1_1"><a href="#__tabbed_1_1" tabindex="-1">pip</a></label><label for="__tabbed_1_2"><a href="#__tabbed_1_2" tabindex="-1">uv</a></label></div>
<div class="tabbed-content">
<div class="tabbed-block">
<div class="language-bash highlight"><pre id="__code_0"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_0 > code"></button><code>pip<span class="w"> </span>install<span class="w"> </span><span class="s2">"pydantic-ai-slim[openai]"</span>
</code></pre></div>
</div>
<div class="tabbed-block">
<div class="language-bash highlight"><pre id="__code_1"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_1 > code"></button><code>uv<span class="w"> </span>add<span class="w"> </span><span class="s2">"pydantic-ai-slim[openai]"</span>
</code></pre></div>
</div>
</div>
<div class="tabbed-control tabbed-control--prev" hidden=""><button class="tabbed-button" tabindex="-1" aria-hidden="true"></button></div><div class="tabbed-control tabbed-control--next" hidden=""><button class="tabbed-button" tabindex="-1" aria-hidden="true"></button></div></div>
<h3 id="configuration">Configuration</h3>
<p>To use <a class="autorefs autorefs-internal" href="../api/models/openai/#pydantic_ai.models.openai.OpenAIModel"><code>OpenAIModel</code></a> through their main API, go to <a href="https://platform.openai.com/">platform.openai.com</a> and follow your nose until you find the place to generate an API key.</p>
<h3 id="environment-variable">Environment variable</h3>
<p>Once you have the API key, you can set it as an environment variable:</p>
<div class="language-bash highlight"><pre id="__code_2"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_2 > code"></button><code><span class="nb">export</span><span class="w"> </span><span class="nv">OPENAI_API_KEY</span><span class="o">=</span><span class="s1">'your-api-key'</span>
</code></pre></div>
<p>You can then use <a class="autorefs autorefs-internal" href="../api/models/openai/#pydantic_ai.models.openai.OpenAIModel"><code>OpenAIModel</code></a> by name:</p>
<div class="language-python highlight"><span class="filename">openai_model_by_name.py</span><pre id="__code_3"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_3 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>

<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="s1">'openai:gpt-4o'</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
<p>Or initialise the model directly with just the model name:</p>
<p></p><div class="language-python highlight"><span class="filename">openai_model_init.py</span><pre id="__code_4"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_4 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.openai</span><span class="w"> </span><span class="kn">import</span> <span class="n">OpenAIModel</span>

<span class="n">model</span> <span class="o">=</span> <span class="n">OpenAIModel</span><span class="p">(</span><span class="s1">'gpt-4o'</span><span class="p">)</span>
<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
By default, the <code>OpenAIModel</code> uses the <a class="autorefs autorefs-internal" href="../api/providers/#pydantic_ai.providers.openai.OpenAIProvider.__init__"><code>OpenAIProvider</code></a>
with the <code>base_url</code> set to <code>https://api.openai.com/v1</code>.<p></p>
<h3 id="provider-argument"><code>provider</code> argument</h3>
<p>You can provide a custom <a class="autorefs autorefs-internal" href="../api/providers/#pydantic_ai.providers.Provider"><code>Provider</code></a> via the <a class="autorefs autorefs-internal" href="../api/models/openai/#pydantic_ai.models.openai.OpenAIModel.__init__"><code>provider</code> argument</a>:</p>
<div class="language-python highlight"><span class="filename">openai_model_provider.py</span><pre id="__code_5"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_5 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.openai</span><span class="w"> </span><span class="kn">import</span> <span class="n">OpenAIModel</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.providers.openai</span><span class="w"> </span><span class="kn">import</span> <span class="n">OpenAIProvider</span>

<span class="n">model</span> <span class="o">=</span> <span class="n">OpenAIModel</span><span class="p">(</span><span class="s1">'gpt-4o'</span><span class="p">,</span> <span class="n">provider</span><span class="o">=</span><span class="n">OpenAIProvider</span><span class="p">(</span><span class="n">api_key</span><span class="o">=</span><span class="s1">'your-api-key'</span><span class="p">))</span>
<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
<h3 id="custom-openai-client">Custom OpenAI Client</h3>
<p><code>OpenAIProvider</code> also accepts a custom <code>AsyncOpenAI</code> client via the
<a class="autorefs autorefs-internal" href="../api/providers/#pydantic_ai.providers.openai.OpenAIProvider.__init__"><code>openai_client</code> parameter</a>, so you can customise the
<code>organization</code>, <code>project</code>, <code>base_url</code> etc. as defined in the <a href="https://platform.openai.com/docs/api-reference">OpenAI API docs</a>.</p>
<p>You could also use the <a href="https://learn.microsoft.com/en-us/azure/ai-services/openai/how-to/switching-endpoints"><code>AsyncAzureOpenAI</code></a>
client to use the Azure OpenAI API.</p>
<div class="language-python highlight"><span class="filename">openai_azure.py</span><pre id="__code_6"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_6 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">openai</span><span class="w"> </span><span class="kn">import</span> <span class="n">AsyncAzureOpenAI</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.openai</span><span class="w"> </span><span class="kn">import</span> <span class="n">OpenAIModel</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.providers.openai</span><span class="w"> </span><span class="kn">import</span> <span class="n">OpenAIProvider</span>

<span class="n">client</span> <span class="o">=</span> <span class="n">AsyncAzureOpenAI</span><span class="p">(</span>
    <span class="n">azure_endpoint</span><span class="o">=</span><span class="s1">'...'</span><span class="p">,</span>
    <span class="n">api_version</span><span class="o">=</span><span class="s1">'2024-07-01-preview'</span><span class="p">,</span>
    <span class="n">api_key</span><span class="o">=</span><span class="s1">'your-api-key'</span><span class="p">,</span>
<span class="p">)</span>

<span class="n">model</span> <span class="o">=</span> <span class="n">OpenAIModel</span><span class="p">(</span>
    <span class="s1">'gpt-4o'</span><span class="p">,</span>
    <span class="n">provider</span><span class="o">=</span><span class="n">OpenAIProvider</span><span class="p">(</span><span class="n">openai_client</span><span class="o">=</span><span class="n">client</span><span class="p">),</span>
<span class="p">)</span>
<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
<h3 id="openai-responses-api">OpenAI Responses API</h3>
<p>PydanticAI also supports OpenAI's <a href="https://platform.openai.com/docs/api-reference/responses">Responses API</a> through the <a class="autorefs autorefs-internal" href="../api/models/openai/#pydantic_ai.models.openai.OpenAIResponsesModel"><code>OpenAIResponsesModel</code></a> class.</p>
<div class="language-python highlight"><span class="filename">openai_responses_model.py</span><pre id="__code_7"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_7 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.openai</span><span class="w"> </span><span class="kn">import</span> <span class="n">OpenAIResponsesModel</span>

<span class="n">model</span> <span class="o">=</span> <span class="n">OpenAIResponsesModel</span><span class="p">(</span><span class="s1">'gpt-4o'</span><span class="p">)</span>
<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
<p>The Responses API has built-in tools that you can use instead of building your own:</p>
<ul>
<li><a href="https://platform.openai.com/docs/guides/tools-web-search">Web search</a>: allow models to search the web for the latest information before generating a response.</li>
<li><a href="https://platform.openai.com/docs/guides/tools-file-search">File search</a>: allow models to search your files for relevant information before generating a response.</li>
<li><a href="https://platform.openai.com/docs/guides/tools-computer-use">Computer use</a>: allow models to use a computer to perform tasks on your behalf.</li>
</ul>
<p>You can use the <a class="autorefs autorefs-internal" href="../api/models/openai/#pydantic_ai.models.openai.OpenAIResponsesModelSettings"><code>OpenAIResponsesModelSettings</code></a>
class to make use of those built-in tools:</p>
<div class="language-python highlight"><span class="filename">openai_responses_model_settings.py</span><pre id="__code_8"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_8 > code"></button><code tabindex="0"><span class="kn">from</span><span class="w"> </span><span class="nn">openai.types.responses</span><span class="w"> </span><span class="kn">import</span> <span class="n">WebSearchToolParam</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 477px; --md-tooltip-y: 20px; --md-tooltip-0: -16px;"><div class="md-tooltip" id="__code_8_annotation_1" role="tooltip"><div class="md-tooltip__inner md-typeset">The file search tool and computer use tool can also be imported from <code>openai.types.responses</code>.</div></div><a href="#__code_8_annotation_1" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="1"></span></a></aside></span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.openai</span><span class="w"> </span><span class="kn">import</span> <span class="n">OpenAIResponsesModel</span><span class="p">,</span> <span class="n">OpenAIResponsesModelSettings</span>

<span class="n">model_settings</span> <span class="o">=</span> <span class="n">OpenAIResponsesModelSettings</span><span class="p">(</span>
    <span class="n">openai_builtin_tools</span><span class="o">=</span><span class="p">[</span><span class="n">WebSearchToolParam</span><span class="p">(</span><span class="nb">type</span><span class="o">=</span><span class="s1">'web_search_preview'</span><span class="p">)],</span>
<span class="p">)</span>
<span class="n">model</span> <span class="o">=</span> <span class="n">OpenAIResponsesModel</span><span class="p">(</span><span class="s1">'gpt-4o'</span><span class="p">)</span>
<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">model</span><span class="o">=</span><span class="n">model</span><span class="p">,</span> <span class="n">model_settings</span><span class="o">=</span><span class="n">model_settings</span><span class="p">)</span>

<span class="n">result</span> <span class="o">=</span> <span class="n">agent</span><span class="o">.</span><span class="n">run_sync</span><span class="p">(</span><span class="s1">'What is the weather in Tokyo?'</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>
<span class="sd">"""</span>
<span class="sd">As of 7:48 AM on Wednesday, April 2, 2025, in Tokyo, Japan, the weather is cloudy with a temperature of 53°F (12°C).</span>
<span class="sd">"""</span>
</code></pre></div>
<ol hidden="">
<li></li>
</ol>
<p>You can learn more about the differences between the Responses API and Chat Completions API in the <a href="https://platform.openai.com/docs/guides/responses-vs-chat-completions">OpenAI API docs</a>.</p>
<h2 id="anthropic">Anthropic</h2>
<h3 id="install_1">Install</h3>
<p>To use <a class="autorefs autorefs-internal" href="../api/models/anthropic/#pydantic_ai.models.anthropic.AnthropicModel"><code>AnthropicModel</code></a> models, you need to either install <a href="../install/"><code>pydantic-ai</code></a>, or install <a href="../install/#slim-install"><code>pydantic-ai-slim</code></a> with the <code>anthropic</code> optional group:</p>
<div class="tabbed-set tabbed-alternate" data-tabs="2:2"><input checked="checked" id="__tabbed_2_1" name="__tabbed_2" type="radio"><input id="__tabbed_2_2" name="__tabbed_2" type="radio"><div class="tabbed-labels tabbed-labels--linked"><label for="__tabbed_2_1"><a href="#__tabbed_2_1" tabindex="-1">pip</a></label><label for="__tabbed_2_2"><a href="#__tabbed_2_2" tabindex="-1">uv</a></label></div>
<div class="tabbed-content">
<div class="tabbed-block">
<div class="language-bash highlight"><pre id="__code_9"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_9 > code"></button><code>pip<span class="w"> </span>install<span class="w"> </span><span class="s2">"pydantic-ai-slim[anthropic]"</span>
</code></pre></div>
</div>
<div class="tabbed-block">
<div class="language-bash highlight"><pre id="__code_10"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_10 > code"></button><code>uv<span class="w"> </span>add<span class="w"> </span><span class="s2">"pydantic-ai-slim[anthropic]"</span>
</code></pre></div>
</div>
</div>
<div class="tabbed-control tabbed-control--prev" hidden=""><button class="tabbed-button" tabindex="-1" aria-hidden="true"></button></div><div class="tabbed-control tabbed-control--next" hidden=""><button class="tabbed-button" tabindex="-1" aria-hidden="true"></button></div></div>
<h3 id="configuration_1">Configuration</h3>
<p>To use <a href="https://anthropic.com">Anthropic</a> through their API, go to <a href="https://console.anthropic.com/settings/keys">console.anthropic.com/settings/keys</a> to generate an API key.</p>
<p><a class="autorefs autorefs-internal" href="../api/models/anthropic/#pydantic_ai.models.anthropic.AnthropicModelName"><code>AnthropicModelName</code></a> contains a list of available Anthropic models.</p>
<h3 id="environment-variable_1">Environment variable</h3>
<p>Once you have the API key, you can set it as an environment variable:</p>
<div class="language-bash highlight"><pre id="__code_11"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_11 > code"></button><code><span class="nb">export</span><span class="w"> </span><span class="nv">ANTHROPIC_API_KEY</span><span class="o">=</span><span class="s1">'your-api-key'</span>
</code></pre></div>
<p>You can then use <a class="autorefs autorefs-internal" href="../api/models/anthropic/#pydantic_ai.models.anthropic.AnthropicModel"><code>AnthropicModel</code></a> by name:</p>
<div class="language-py highlight"><span class="filename">anthropic_model_by_name.py</span><pre id="__code_12"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_12 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>

<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="s1">'anthropic:claude-3-5-sonnet-latest'</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
<p>Or initialise the model directly with just the model name:</p>
<div class="language-py highlight"><span class="filename">anthropic_model_init.py</span><pre id="__code_13"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_13 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.anthropic</span><span class="w"> </span><span class="kn">import</span> <span class="n">AnthropicModel</span>

<span class="n">model</span> <span class="o">=</span> <span class="n">AnthropicModel</span><span class="p">(</span><span class="s1">'claude-3-5-sonnet-latest'</span><span class="p">)</span>
<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
<h3 id="provider-argument_1"><code>provider</code> argument</h3>
<p>You can provide a custom <a class="autorefs autorefs-internal" href="../api/providers/#pydantic_ai.providers.Provider"><code>Provider</code></a> via the <a class="autorefs autorefs-internal" href="../api/models/anthropic/#pydantic_ai.models.anthropic.AnthropicModel.__init__"><code>provider</code> argument</a>:</p>
<div class="language-py highlight"><span class="filename">anthropic_model_provider.py</span><pre id="__code_14"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_14 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.anthropic</span><span class="w"> </span><span class="kn">import</span> <span class="n">AnthropicModel</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.providers.anthropic</span><span class="w"> </span><span class="kn">import</span> <span class="n">AnthropicProvider</span>

<span class="n">model</span> <span class="o">=</span> <span class="n">AnthropicModel</span><span class="p">(</span>
    <span class="s1">'claude-3-5-sonnet-latest'</span><span class="p">,</span> <span class="n">provider</span><span class="o">=</span><span class="n">AnthropicProvider</span><span class="p">(</span><span class="n">api_key</span><span class="o">=</span><span class="s1">'your-api-key'</span><span class="p">)</span>
<span class="p">)</span>
<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
<h3 id="custom-http-client">Custom HTTP Client</h3>
<p>You can customize the <code>AnthropicProvider</code> with a custom <code>httpx.AsyncClient</code>:</p>
<div class="language-py highlight"><span class="filename">anthropic_model_custom_provider.py</span><pre id="__code_15"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_15 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">httpx</span><span class="w"> </span><span class="kn">import</span> <span class="n">AsyncClient</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.anthropic</span><span class="w"> </span><span class="kn">import</span> <span class="n">AnthropicModel</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.providers.anthropic</span><span class="w"> </span><span class="kn">import</span> <span class="n">AnthropicProvider</span>

<span class="n">custom_http_client</span> <span class="o">=</span> <span class="n">AsyncClient</span><span class="p">(</span><span class="n">timeout</span><span class="o">=</span><span class="mi">30</span><span class="p">)</span>
<span class="n">model</span> <span class="o">=</span> <span class="n">AnthropicModel</span><span class="p">(</span>
    <span class="s1">'claude-3-5-sonnet-latest'</span><span class="p">,</span>
    <span class="n">provider</span><span class="o">=</span><span class="n">AnthropicProvider</span><span class="p">(</span><span class="n">api_key</span><span class="o">=</span><span class="s1">'your-api-key'</span><span class="p">,</span> <span class="n">http_client</span><span class="o">=</span><span class="n">custom_http_client</span><span class="p">),</span>
<span class="p">)</span>
<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
<h2 id="gemini">Gemini</h2>
<h3 id="install_2">Install</h3>
<p>To use <a class="autorefs autorefs-internal" href="../api/models/gemini/#pydantic_ai.models.gemini.GeminiModel"><code>GeminiModel</code></a> models, you just need to install <a href="../install/"><code>pydantic-ai</code></a> or <a href="../install/#slim-install"><code>pydantic-ai-slim</code></a>, no extra dependencies are required.</p>
<h3 id="configuration_2">Configuration</h3>
<p><a class="autorefs autorefs-internal" href="../api/models/gemini/#pydantic_ai.models.gemini.GeminiModel"><code>GeminiModel</code></a> let's you use the Google's Gemini models through their <a href="https://ai.google.dev/api/all-methods">Generative Language API</a>, <code>generativelanguage.googleapis.com</code>.</p>
<p><a class="autorefs autorefs-internal" href="../api/models/gemini/#pydantic_ai.models.gemini.GeminiModelName"><code>GeminiModelName</code></a> contains a list of available Gemini models that can be used through this interface.</p>
<p>To use <code>GeminiModel</code>, go to <a href="https://aistudio.google.com/apikey">aistudio.google.com</a> and select "Create API key".</p>
<h3 id="environment-variable_2">Environment variable</h3>
<p>Once you have the API key, you can set it as an environment variable:</p>
<div class="language-bash highlight"><pre id="__code_16"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_16 > code"></button><code><span class="nb">export</span><span class="w"> </span><span class="nv">GEMINI_API_KEY</span><span class="o">=</span>your-api-key
</code></pre></div>
<p>You can then use <a class="autorefs autorefs-internal" href="../api/models/gemini/#pydantic_ai.models.gemini.GeminiModel"><code>GeminiModel</code></a> by name:</p>
<div class="language-python highlight"><span class="filename">gemini_model_by_name.py</span><pre id="__code_17"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_17 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>

<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="s1">'google-gla:gemini-2.0-flash'</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The <code>google-gla</code> provider prefix represents the <a href="https://ai.google.dev/api/all-methods">Google <strong>G</strong>enerative <strong>L</strong>anguage <strong>A</strong>PI</a> for <code>GeminiModel</code>s.
<code>google-vertex</code> is used with <a href="https://cloud.google.com/vertex-ai/generative-ai/docs/learn/models">Vertex AI</a>.</p>
</div>
<p>Or initialise the model directly with just the model name and provider:</p>
<div class="language-python highlight"><span class="filename">gemini_model_init.py</span><pre id="__code_18"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_18 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.gemini</span><span class="w"> </span><span class="kn">import</span> <span class="n">GeminiModel</span>

<span class="n">model</span> <span class="o">=</span> <span class="n">GeminiModel</span><span class="p">(</span><span class="s1">'gemini-2.0-flash'</span><span class="p">,</span> <span class="n">provider</span><span class="o">=</span><span class="s1">'google-gla'</span><span class="p">)</span>
<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
<h3 id="provider-argument_2"><code>provider</code> argument</h3>
<p>You can provide a custom <a class="autorefs autorefs-internal" href="../api/providers/#pydantic_ai.providers.Provider"><code>Provider</code></a> via the <a class="autorefs autorefs-internal" href="../api/models/gemini/#pydantic_ai.models.gemini.GeminiModel.__init__"><code>provider</code> argument</a>:</p>
<p></p><div class="language-python highlight"><span class="filename">gemini_model_provider.py</span><pre id="__code_19"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_19 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.gemini</span><span class="w"> </span><span class="kn">import</span> <span class="n">GeminiModel</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.providers.google_gla</span><span class="w"> </span><span class="kn">import</span> <span class="n">GoogleGLAProvider</span>

<span class="n">model</span> <span class="o">=</span> <span class="n">GeminiModel</span><span class="p">(</span>
    <span class="s1">'gemini-2.0-flash'</span><span class="p">,</span> <span class="n">provider</span><span class="o">=</span><span class="n">GoogleGLAProvider</span><span class="p">(</span><span class="n">api_key</span><span class="o">=</span><span class="s1">'your-api-key'</span><span class="p">)</span>
<span class="p">)</span>
<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
You can also customize the <code>GoogleGLAProvider</code> with a custom <code>http_client</code>:
<div class="language-python highlight"><span class="filename">gemini_model_custom_provider.py</span><pre id="__code_20"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_20 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">httpx</span><span class="w"> </span><span class="kn">import</span> <span class="n">AsyncClient</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.gemini</span><span class="w"> </span><span class="kn">import</span> <span class="n">GeminiModel</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.providers.google_gla</span><span class="w"> </span><span class="kn">import</span> <span class="n">GoogleGLAProvider</span>

<span class="n">custom_http_client</span> <span class="o">=</span> <span class="n">AsyncClient</span><span class="p">(</span><span class="n">timeout</span><span class="o">=</span><span class="mi">30</span><span class="p">)</span>
<span class="n">model</span> <span class="o">=</span> <span class="n">GeminiModel</span><span class="p">(</span>
    <span class="s1">'gemini-2.0-flash'</span><span class="p">,</span>
    <span class="n">provider</span><span class="o">=</span><span class="n">GoogleGLAProvider</span><span class="p">(</span><span class="n">api_key</span><span class="o">=</span><span class="s1">'your-api-key'</span><span class="p">,</span> <span class="n">http_client</span><span class="o">=</span><span class="n">custom_http_client</span><span class="p">),</span>
<span class="p">)</span>
<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div><p></p>
<h2 id="gemini-via-vertexai">Gemini via VertexAI</h2>
<p>If you are an enterprise user, you should use the <code>google-vertex</code> provider with <a class="autorefs autorefs-internal" href="../api/models/gemini/#pydantic_ai.models.gemini.GeminiModel"><code>GeminiModel</code></a> which uses the <code>*-aiplatform.googleapis.com</code> API.</p>
<p><a class="autorefs autorefs-internal" href="../api/models/gemini/#pydantic_ai.models.gemini.GeminiModelName"><code>GeminiModelName</code></a> contains a list of available Gemini models that can be used through this interface.</p>
<h3 id="install_3">Install</h3>
<p>To use the <code>google-vertex</code> provider with <a class="autorefs autorefs-internal" href="../api/models/gemini/#pydantic_ai.models.gemini.GeminiModel"><code>GeminiModel</code></a>, you need to either install
<a href="../install/"><code>pydantic-ai</code></a>, or install <a href="../install/#slim-install"><code>pydantic-ai-slim</code></a> with the <code>vertexai</code> optional group:</p>
<div class="tabbed-set tabbed-alternate" data-tabs="3:2"><input checked="checked" id="__tabbed_3_1" name="__tabbed_3" type="radio"><input id="__tabbed_3_2" name="__tabbed_3" type="radio"><div class="tabbed-labels tabbed-labels--linked"><label for="__tabbed_3_1"><a href="#__tabbed_3_1" tabindex="-1">pip</a></label><label for="__tabbed_3_2"><a href="#__tabbed_3_2" tabindex="-1">uv</a></label></div>
<div class="tabbed-content">
<div class="tabbed-block">
<div class="language-bash highlight"><pre id="__code_21"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_21 > code"></button><code>pip<span class="w"> </span>install<span class="w"> </span><span class="s2">"pydantic-ai-slim[vertexai]"</span>
</code></pre></div>
</div>
<div class="tabbed-block">
<div class="language-bash highlight"><pre id="__code_22"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_22 > code"></button><code>uv<span class="w"> </span>add<span class="w"> </span><span class="s2">"pydantic-ai-slim[vertexai]"</span>
</code></pre></div>
</div>
</div>
<div class="tabbed-control tabbed-control--prev" hidden=""><button class="tabbed-button" tabindex="-1" aria-hidden="true"></button></div><div class="tabbed-control tabbed-control--next" hidden=""><button class="tabbed-button" tabindex="-1" aria-hidden="true"></button></div></div>
<h3 id="configuration_3">Configuration</h3>
<p>This interface has a number of advantages over <code>generativelanguage.googleapis.com</code> documented above:</p>
<ol>
<li>The VertexAI API comes with more enterprise readiness guarantees.</li>
<li>You can
   <a href="https://cloud.google.com/vertex-ai/generative-ai/docs/provisioned-throughput#purchase-provisioned-throughput">purchase provisioned throughput</a>
   with VertexAI to guarantee capacity.</li>
<li>If you're running PydanticAI inside GCP, you don't need to set up authentication, it should "just work".</li>
<li>You can decide which region to use, which might be important from a regulatory perspective,
   and might improve latency.</li>
</ol>
<p>The big disadvantage is that for local development you may need to create and configure a "service account", which I've found extremely painful to get right in the past.</p>
<p>Whichever way you authenticate, you'll need to have VertexAI enabled in your GCP account.</p>
<h3 id="application-default-credentials">Application default credentials</h3>
<p>Luckily if you're running PydanticAI inside GCP, or you have the <a href="https://cloud.google.com/sdk/gcloud"><code>gcloud</code> CLI</a> installed and configured, you should be able to use <code>VertexAIModel</code> without any additional setup.</p>
<p>To use <code>VertexAIModel</code>, with <a href="https://cloud.google.com/docs/authentication/application-default-credentials">application default credentials</a> configured (e.g. with <code>gcloud</code>), you can simply use:</p>
<div class="language-python highlight"><span class="filename">vertexai_application_default_credentials.py</span><pre id="__code_23"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_23 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.gemini</span><span class="w"> </span><span class="kn">import</span> <span class="n">GeminiModel</span>

<span class="n">model</span> <span class="o">=</span> <span class="n">GeminiModel</span><span class="p">(</span><span class="s1">'gemini-2.0-flash'</span><span class="p">,</span> <span class="n">provider</span><span class="o">=</span><span class="s1">'google-vertex'</span><span class="p">)</span>
<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
<p>Internally this uses <a href="https://google-auth.readthedocs.io/en/master/reference/google.auth.html"><code>google.auth.default()</code></a> from the <code>google-auth</code> package to obtain credentials.</p>
<div class="admonition note">
<p class="admonition-title">Won't fail until <code>agent.run()</code></p>
<p>Because <code>google.auth.default()</code> requires network requests and can be slow, it's not run until you call <code>agent.run()</code>.</p>
</div>
<p>You may also need to pass the <a class="autorefs autorefs-internal" href="../api/providers/#pydantic_ai.providers.google_vertex.GoogleVertexProvider"><code>project_id</code> argument to <code>GoogleVertexProvider</code></a> if application default credentials don't set a project, if you pass <code>project_id</code> and it conflicts with the project set by application default credentials, an error is raised.</p>
<h3 id="service-account">Service account</h3>
<p>If instead of application default credentials, you want to authenticate with a service account, you'll need to create a service account, add it to your GCP project (note: AFAIK this step is necessary even if you created the service account within the project), give that service account the "Vertex AI Service Agent" role, and download the service account JSON file.</p>
<p>Once you have the JSON file, you can use it thus:</p>
<div class="language-python highlight"><span class="filename">vertexai_service_account.py</span><pre id="__code_24"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_24 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.gemini</span><span class="w"> </span><span class="kn">import</span> <span class="n">GeminiModel</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.providers.google_vertex</span><span class="w"> </span><span class="kn">import</span> <span class="n">GoogleVertexProvider</span>

<span class="n">model</span> <span class="o">=</span> <span class="n">GeminiModel</span><span class="p">(</span>
    <span class="s1">'gemini-2.0-flash'</span><span class="p">,</span>
    <span class="n">provider</span><span class="o">=</span><span class="n">GoogleVertexProvider</span><span class="p">(</span><span class="n">service_account_file</span><span class="o">=</span><span class="s1">'path/to/service-account.json'</span><span class="p">),</span>
<span class="p">)</span>
<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
<p>Alternatively, if you already have the service account information in memory, you can pass it as a dictionary:</p>
<div class="language-python highlight"><span class="filename">vertexai_service_account.py</span><pre id="__code_25"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_25 > code"></button><code><span class="kn">import</span><span class="w"> </span><span class="nn">json</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.gemini</span><span class="w"> </span><span class="kn">import</span> <span class="n">GeminiModel</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.providers.google_vertex</span><span class="w"> </span><span class="kn">import</span> <span class="n">GoogleVertexProvider</span>

<span class="hll"><span class="n">service_account_info</span> <span class="o">=</span> <span class="n">json</span><span class="o">.</span><span class="n">loads</span><span class="p">(</span>
</span><span class="hll">    <span class="s1">'{"type": "service_account", "project_id": "my-project-id"}'</span>
</span><span class="hll"><span class="p">)</span>
</span><span class="n">model</span> <span class="o">=</span> <span class="n">GeminiModel</span><span class="p">(</span>
    <span class="s1">'gemini-2.0-flash'</span><span class="p">,</span>
    <span class="n">provider</span><span class="o">=</span><span class="n">GoogleVertexProvider</span><span class="p">(</span><span class="n">service_account_info</span><span class="o">=</span><span class="n">service_account_info</span><span class="p">),</span>
<span class="p">)</span>
<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
<h3 id="customising-region">Customising region</h3>
<p>Whichever way you authenticate, you can specify which region requests will be sent to via the <a class="autorefs autorefs-internal" href="../api/providers/#pydantic_ai.providers.google_vertex.GoogleVertexProvider"><code>region</code> argument</a>.</p>
<p>Using a region close to your application can improve latency and might be important from a regulatory perspective.</p>
<p></p><div class="language-python highlight"><span class="filename">vertexai_region.py</span><pre id="__code_26"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_26 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.gemini</span><span class="w"> </span><span class="kn">import</span> <span class="n">GeminiModel</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.providers.google_vertex</span><span class="w"> </span><span class="kn">import</span> <span class="n">GoogleVertexProvider</span>

<span class="n">model</span> <span class="o">=</span> <span class="n">GeminiModel</span><span class="p">(</span>
    <span class="s1">'gemini-2.0-flash'</span><span class="p">,</span> <span class="n">provider</span><span class="o">=</span><span class="n">GoogleVertexProvider</span><span class="p">(</span><span class="n">region</span><span class="o">=</span><span class="s1">'asia-east1'</span><span class="p">)</span>
<span class="p">)</span>
<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
You can also customize the <code>GoogleVertexProvider</code> with a custom <code>http_client</code>:
<div class="language-python highlight"><span class="filename">vertexai_custom_provider.py</span><pre id="__code_27"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_27 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">httpx</span><span class="w"> </span><span class="kn">import</span> <span class="n">AsyncClient</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.gemini</span><span class="w"> </span><span class="kn">import</span> <span class="n">GeminiModel</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.providers.google_vertex</span><span class="w"> </span><span class="kn">import</span> <span class="n">GoogleVertexProvider</span>

<span class="n">custom_http_client</span> <span class="o">=</span> <span class="n">AsyncClient</span><span class="p">(</span><span class="n">timeout</span><span class="o">=</span><span class="mi">30</span><span class="p">)</span>
<span class="n">model</span> <span class="o">=</span> <span class="n">GeminiModel</span><span class="p">(</span>
    <span class="s1">'gemini-2.0-flash'</span><span class="p">,</span>
    <span class="n">provider</span><span class="o">=</span><span class="n">GoogleVertexProvider</span><span class="p">(</span><span class="n">region</span><span class="o">=</span><span class="s1">'asia-east1'</span><span class="p">,</span> <span class="n">http_client</span><span class="o">=</span><span class="n">custom_http_client</span><span class="p">),</span>
<span class="p">)</span>
<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div><p></p>
<h2 id="groq">Groq</h2>
<h3 id="install_4">Install</h3>
<p>To use <a class="autorefs autorefs-internal" href="../api/models/groq/#pydantic_ai.models.groq.GroqModel"><code>GroqModel</code></a>, you need to either install <a href="../install/"><code>pydantic-ai</code></a>, or install <a href="../install/#slim-install"><code>pydantic-ai-slim</code></a> with the <code>groq</code> optional group:</p>
<div class="tabbed-set tabbed-alternate" data-tabs="4:2"><input checked="checked" id="__tabbed_4_1" name="__tabbed_4" type="radio"><input id="__tabbed_4_2" name="__tabbed_4" type="radio"><div class="tabbed-labels tabbed-labels--linked"><label for="__tabbed_4_1"><a href="#__tabbed_4_1" tabindex="-1">pip</a></label><label for="__tabbed_4_2"><a href="#__tabbed_4_2" tabindex="-1">uv</a></label></div>
<div class="tabbed-content">
<div class="tabbed-block">
<div class="language-bash highlight"><pre id="__code_28"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_28 > code"></button><code>pip<span class="w"> </span>install<span class="w"> </span><span class="s2">"pydantic-ai-slim[groq]"</span>
</code></pre></div>
</div>
<div class="tabbed-block">
<div class="language-bash highlight"><pre id="__code_29"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_29 > code"></button><code>uv<span class="w"> </span>add<span class="w"> </span><span class="s2">"pydantic-ai-slim[groq]"</span>
</code></pre></div>
</div>
</div>
<div class="tabbed-control tabbed-control--prev" hidden=""><button class="tabbed-button" tabindex="-1" aria-hidden="true"></button></div><div class="tabbed-control tabbed-control--next" hidden=""><button class="tabbed-button" tabindex="-1" aria-hidden="true"></button></div></div>
<h3 id="configuration_4">Configuration</h3>
<p>To use <a href="https://groq.com/">Groq</a> through their API, go to <a href="https://console.groq.com/keys">console.groq.com/keys</a> and follow your nose until you find the place to generate an API key.</p>
<p><a class="autorefs autorefs-internal" href="../api/models/groq/#pydantic_ai.models.groq.GroqModelName"><code>GroqModelName</code></a> contains a list of available Groq models.</p>
<h3 id="environment-variable_3">Environment variable</h3>
<p>Once you have the API key, you can set it as an environment variable:</p>
<div class="language-bash highlight"><pre id="__code_30"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_30 > code"></button><code><span class="nb">export</span><span class="w"> </span><span class="nv">GROQ_API_KEY</span><span class="o">=</span><span class="s1">'your-api-key'</span>
</code></pre></div>
<p>You can then use <a class="autorefs autorefs-internal" href="../api/models/groq/#pydantic_ai.models.groq.GroqModel"><code>GroqModel</code></a> by name:</p>
<div class="language-python highlight"><span class="filename">groq_model_by_name.py</span><pre id="__code_31"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_31 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>

<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="s1">'groq:llama-3.3-70b-versatile'</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
<p>Or initialise the model directly with just the model name:</p>
<div class="language-python highlight"><span class="filename">groq_model_init.py</span><pre id="__code_32"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_32 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.groq</span><span class="w"> </span><span class="kn">import</span> <span class="n">GroqModel</span>

<span class="n">model</span> <span class="o">=</span> <span class="n">GroqModel</span><span class="p">(</span><span class="s1">'llama-3.3-70b-versatile'</span><span class="p">)</span>
<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
<h3 id="provider-argument_3"><code>provider</code> argument</h3>
<p>You can provide a custom <a class="autorefs autorefs-internal" href="../api/providers/#pydantic_ai.providers.Provider"><code>Provider</code></a> via the
<a class="autorefs autorefs-internal" href="../api/models/groq/#pydantic_ai.models.groq.GroqModel.__init__"><code>provider</code> argument</a>:</p>
<div class="language-python highlight"><span class="filename">groq_model_provider.py</span><pre id="__code_33"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_33 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.groq</span><span class="w"> </span><span class="kn">import</span> <span class="n">GroqModel</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.providers.groq</span><span class="w"> </span><span class="kn">import</span> <span class="n">GroqProvider</span>

<span class="n">model</span> <span class="o">=</span> <span class="n">GroqModel</span><span class="p">(</span>
    <span class="s1">'llama-3.3-70b-versatile'</span><span class="p">,</span> <span class="n">provider</span><span class="o">=</span><span class="n">GroqProvider</span><span class="p">(</span><span class="n">api_key</span><span class="o">=</span><span class="s1">'your-api-key'</span><span class="p">)</span>
<span class="p">)</span>
<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
<p>You can also customize the <a class="autorefs autorefs-internal" href="../api/providers/#pydantic_ai.providers.groq.GroqProvider"><code>GroqProvider</code></a> with a
custom <code>httpx.AsyncHTTPClient</code>:</p>
<div class="language-python highlight"><span class="filename">groq_model_custom_provider.py</span><pre id="__code_34"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_34 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">httpx</span><span class="w"> </span><span class="kn">import</span> <span class="n">AsyncClient</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.groq</span><span class="w"> </span><span class="kn">import</span> <span class="n">GroqModel</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.providers.groq</span><span class="w"> </span><span class="kn">import</span> <span class="n">GroqProvider</span>

<span class="n">custom_http_client</span> <span class="o">=</span> <span class="n">AsyncClient</span><span class="p">(</span><span class="n">timeout</span><span class="o">=</span><span class="mi">30</span><span class="p">)</span>
<span class="n">model</span> <span class="o">=</span> <span class="n">GroqModel</span><span class="p">(</span>
    <span class="s1">'llama-3.3-70b-versatile'</span><span class="p">,</span>
    <span class="n">provider</span><span class="o">=</span><span class="n">GroqProvider</span><span class="p">(</span><span class="n">api_key</span><span class="o">=</span><span class="s1">'your-api-key'</span><span class="p">,</span> <span class="n">http_client</span><span class="o">=</span><span class="n">custom_http_client</span><span class="p">),</span>
<span class="p">)</span>
<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
<h2 id="mistral">Mistral</h2>
<h3 id="install_5">Install</h3>
<p>To use <a class="autorefs autorefs-internal" href="../api/models/mistral/#pydantic_ai.models.mistral.MistralModel"><code>MistralModel</code></a>, you need to either install <a href="../install/"><code>pydantic-ai</code></a>, or install <a href="../install/#slim-install"><code>pydantic-ai-slim</code></a> with the <code>mistral</code> optional group:</p>
<div class="tabbed-set tabbed-alternate" data-tabs="5:2"><input checked="checked" id="__tabbed_5_1" name="__tabbed_5" type="radio"><input id="__tabbed_5_2" name="__tabbed_5" type="radio"><div class="tabbed-labels tabbed-labels--linked"><label for="__tabbed_5_1"><a href="#__tabbed_5_1" tabindex="-1">pip</a></label><label for="__tabbed_5_2"><a href="#__tabbed_5_2" tabindex="-1">uv</a></label></div>
<div class="tabbed-content">
<div class="tabbed-block">
<div class="language-bash highlight"><pre id="__code_35"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_35 > code"></button><code>pip<span class="w"> </span>install<span class="w"> </span><span class="s2">"pydantic-ai-slim[mistral]"</span>
</code></pre></div>
</div>
<div class="tabbed-block">
<div class="language-bash highlight"><pre id="__code_36"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_36 > code"></button><code>uv<span class="w"> </span>add<span class="w"> </span><span class="s2">"pydantic-ai-slim[mistral]"</span>
</code></pre></div>
</div>
</div>
<div class="tabbed-control tabbed-control--prev" hidden=""><button class="tabbed-button" tabindex="-1" aria-hidden="true"></button></div><div class="tabbed-control tabbed-control--next" hidden=""><button class="tabbed-button" tabindex="-1" aria-hidden="true"></button></div></div>
<h3 id="configuration_5">Configuration</h3>
<p>To use <a href="https://mistral.ai">Mistral</a> through their API, go to <a href="https://console.mistral.ai/api-keys/">console.mistral.ai/api-keys/</a> and follow your nose until you find the place to generate an API key.</p>
<p><a class="autorefs autorefs-internal" href="../api/models/mistral/#pydantic_ai.models.mistral.LatestMistralModelNames"><code>LatestMistralModelNames</code></a> contains a list of the most popular Mistral models.</p>
<h3 id="environment-variable_4">Environment variable</h3>
<p>Once you have the API key, you can set it as an environment variable:</p>
<div class="language-bash highlight"><pre id="__code_37"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_37 > code"></button><code><span class="nb">export</span><span class="w"> </span><span class="nv">MISTRAL_API_KEY</span><span class="o">=</span><span class="s1">'your-api-key'</span>
</code></pre></div>
<p>You can then use <a class="autorefs autorefs-internal" href="../api/models/mistral/#pydantic_ai.models.mistral.MistralModel"><code>MistralModel</code></a> by name:</p>
<div class="language-python highlight"><span class="filename">mistral_model_by_name.py</span><pre id="__code_38"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_38 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>

<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="s1">'mistral:mistral-large-latest'</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
<p>Or initialise the model directly with just the model name:</p>
<div class="language-python highlight"><span class="filename">mistral_model_init.py</span><pre id="__code_39"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_39 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.mistral</span><span class="w"> </span><span class="kn">import</span> <span class="n">MistralModel</span>

<span class="n">model</span> <span class="o">=</span> <span class="n">MistralModel</span><span class="p">(</span><span class="s1">'mistral-small-latest'</span><span class="p">)</span>
<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
<h3 id="provider-argument_4"><code>provider</code> argument</h3>
<p>You can provide a custom <a class="autorefs autorefs-internal" href="../api/providers/#pydantic_ai.providers.Provider"><code>Provider</code></a> via the
<a class="autorefs autorefs-internal" href="../api/models/mistral/#pydantic_ai.models.mistral.MistralModel.__init__"><code>provider</code> argument</a>:</p>
<div class="language-python highlight"><span class="filename">groq_model_provider.py</span><pre id="__code_40"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_40 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.mistral</span><span class="w"> </span><span class="kn">import</span> <span class="n">MistralModel</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.providers.mistral</span><span class="w"> </span><span class="kn">import</span> <span class="n">MistralProvider</span>

<span class="n">model</span> <span class="o">=</span> <span class="n">MistralModel</span><span class="p">(</span>
    <span class="s1">'mistral-large-latest'</span><span class="p">,</span> <span class="n">provider</span><span class="o">=</span><span class="n">MistralProvider</span><span class="p">(</span><span class="n">api_key</span><span class="o">=</span><span class="s1">'your-api-key'</span><span class="p">)</span>
<span class="p">)</span>
<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
<p>You can also customize the provider with a custom <code>httpx.AsyncHTTPClient</code>:</p>
<div class="language-python highlight"><span class="filename">groq_model_custom_provider.py</span><pre id="__code_41"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_41 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">httpx</span><span class="w"> </span><span class="kn">import</span> <span class="n">AsyncClient</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.mistral</span><span class="w"> </span><span class="kn">import</span> <span class="n">MistralModel</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.providers.mistral</span><span class="w"> </span><span class="kn">import</span> <span class="n">MistralProvider</span>

<span class="n">custom_http_client</span> <span class="o">=</span> <span class="n">AsyncClient</span><span class="p">(</span><span class="n">timeout</span><span class="o">=</span><span class="mi">30</span><span class="p">)</span>
<span class="n">model</span> <span class="o">=</span> <span class="n">MistralModel</span><span class="p">(</span>
    <span class="s1">'mistral-large-latest'</span><span class="p">,</span>
    <span class="n">provider</span><span class="o">=</span><span class="n">MistralProvider</span><span class="p">(</span><span class="n">api_key</span><span class="o">=</span><span class="s1">'your-api-key'</span><span class="p">,</span> <span class="n">http_client</span><span class="o">=</span><span class="n">custom_http_client</span><span class="p">),</span>
<span class="p">)</span>
<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
<h2 id="cohere">Cohere</h2>
<h3 id="install_6">Install</h3>
<p>To use <a class="autorefs autorefs-internal" href="../api/models/cohere/#pydantic_ai.models.cohere.CohereModel"><code>CohereModel</code></a>, you need to either install <a href="../install/"><code>pydantic-ai</code></a>, or install <a href="../install/#slim-install"><code>pydantic-ai-slim</code></a> with the <code>cohere</code> optional group:</p>
<div class="tabbed-set tabbed-alternate" data-tabs="6:2"><input checked="checked" id="__tabbed_6_1" name="__tabbed_6" type="radio"><input id="__tabbed_6_2" name="__tabbed_6" type="radio"><div class="tabbed-labels tabbed-labels--linked"><label for="__tabbed_6_1"><a href="#__tabbed_6_1" tabindex="-1">pip</a></label><label for="__tabbed_6_2"><a href="#__tabbed_6_2" tabindex="-1">uv</a></label></div>
<div class="tabbed-content">
<div class="tabbed-block">
<div class="language-bash highlight"><pre id="__code_42"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_42 > code"></button><code>pip<span class="w"> </span>install<span class="w"> </span><span class="s2">"pydantic-ai-slim[cohere]"</span>
</code></pre></div>
</div>
<div class="tabbed-block">
<div class="language-bash highlight"><pre id="__code_43"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_43 > code"></button><code>uv<span class="w"> </span>add<span class="w"> </span><span class="s2">"pydantic-ai-slim[cohere]"</span>
</code></pre></div>
</div>
</div>
<div class="tabbed-control tabbed-control--prev" hidden=""><button class="tabbed-button" tabindex="-1" aria-hidden="true"></button></div><div class="tabbed-control tabbed-control--next" hidden=""><button class="tabbed-button" tabindex="-1" aria-hidden="true"></button></div></div>
<h3 id="configuration_6">Configuration</h3>
<p>To use <a href="https://cohere.com/">Cohere</a> through their API, go to <a href="https://dashboard.cohere.com/api-keys">dashboard.cohere.com/api-keys</a> and follow your nose until you find the place to generate an API key.</p>
<p><a class="autorefs autorefs-internal" href="../api/models/cohere/#pydantic_ai.models.cohere.CohereModelName"><code>CohereModelName</code></a> contains a list of the most popular Cohere models.</p>
<h3 id="environment-variable_5">Environment variable</h3>
<p>Once you have the API key, you can set it as an environment variable:</p>
<div class="language-bash highlight"><pre id="__code_44"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_44 > code"></button><code><span class="nb">export</span><span class="w"> </span><span class="nv">CO_API_KEY</span><span class="o">=</span><span class="s1">'your-api-key'</span>
</code></pre></div>
<p>You can then use <a class="autorefs autorefs-internal" href="../api/models/cohere/#pydantic_ai.models.cohere.CohereModel"><code>CohereModel</code></a> by name:</p>
<div class="language-python highlight"><span class="filename">cohere_model_by_name.py</span><pre id="__code_45"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_45 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>

<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="s1">'cohere:command'</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
<p>Or initialise the model directly with just the model name:</p>
<div class="language-python highlight"><span class="filename">cohere_model_init.py</span><pre id="__code_46"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_46 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.cohere</span><span class="w"> </span><span class="kn">import</span> <span class="n">CohereModel</span>

<span class="n">model</span> <span class="o">=</span> <span class="n">CohereModel</span><span class="p">(</span><span class="s1">'command'</span><span class="p">)</span>
<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
<h3 id="provider-argument_5"><code>provider</code> argument</h3>
<p>You can provide a custom <a class="autorefs autorefs-internal" href="../api/providers/#pydantic_ai.providers.Provider"><code>Provider</code></a> via the <a class="autorefs autorefs-internal" href="../api/models/cohere/#pydantic_ai.models.cohere.CohereModel.__init__"><code>provider</code> argument</a>:</p>
<div class="language-python highlight"><span class="filename">cohere_model_provider.py</span><pre id="__code_47"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_47 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.cohere</span><span class="w"> </span><span class="kn">import</span> <span class="n">CohereModel</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.providers.cohere</span><span class="w"> </span><span class="kn">import</span> <span class="n">CohereProvider</span>

<span class="n">model</span> <span class="o">=</span> <span class="n">CohereModel</span><span class="p">(</span><span class="s1">'command'</span><span class="p">,</span> <span class="n">provider</span><span class="o">=</span><span class="n">CohereProvider</span><span class="p">(</span><span class="n">api_key</span><span class="o">=</span><span class="s1">'your-api-key'</span><span class="p">))</span>
<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
<p>You can also customize the <code>CohereProvider</code> with a custom <code>http_client</code>:</p>
<div class="language-python highlight"><span class="filename">cohere_model_custom_provider.py</span><pre id="__code_48"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_48 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">httpx</span><span class="w"> </span><span class="kn">import</span> <span class="n">AsyncClient</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.cohere</span><span class="w"> </span><span class="kn">import</span> <span class="n">CohereModel</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.providers.cohere</span><span class="w"> </span><span class="kn">import</span> <span class="n">CohereProvider</span>

<span class="n">custom_http_client</span> <span class="o">=</span> <span class="n">AsyncClient</span><span class="p">(</span><span class="n">timeout</span><span class="o">=</span><span class="mi">30</span><span class="p">)</span>
<span class="n">model</span> <span class="o">=</span> <span class="n">CohereModel</span><span class="p">(</span>
    <span class="s1">'command'</span><span class="p">,</span>
    <span class="n">provider</span><span class="o">=</span><span class="n">CohereProvider</span><span class="p">(</span><span class="n">api_key</span><span class="o">=</span><span class="s1">'your-api-key'</span><span class="p">,</span> <span class="n">http_client</span><span class="o">=</span><span class="n">custom_http_client</span><span class="p">),</span>
<span class="p">)</span>
<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
<h2 id="bedrock">Bedrock</h2>
<h3 id="install_7">Install</h3>
<p>To use <a class="autorefs autorefs-internal" href="../api/models/bedrock/#pydantic_ai.models.bedrock.BedrockConverseModel"><code>BedrockConverseModel</code></a>, you need to either install <a href="../install/"><code>pydantic-ai</code></a>, or install <a href="../install/#slim-install"><code>pydantic-ai-slim</code></a> with the <code>bedrock</code> optional group:</p>
<div class="tabbed-set tabbed-alternate" data-tabs="7:2"><input checked="checked" id="__tabbed_7_1" name="__tabbed_7" type="radio"><input id="__tabbed_7_2" name="__tabbed_7" type="radio"><div class="tabbed-labels tabbed-labels--linked"><label for="__tabbed_7_1"><a href="#__tabbed_7_1" tabindex="-1">pip</a></label><label for="__tabbed_7_2"><a href="#__tabbed_7_2" tabindex="-1">uv</a></label></div>
<div class="tabbed-content">
<div class="tabbed-block">
<div class="language-bash highlight"><pre id="__code_49"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_49 > code"></button><code>pip<span class="w"> </span>install<span class="w"> </span><span class="s2">"pydantic-ai-slim[bedrock]"</span>
</code></pre></div>
</div>
<div class="tabbed-block">
<div class="language-bash highlight"><pre id="__code_50"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_50 > code"></button><code>uv<span class="w"> </span>add<span class="w"> </span><span class="s2">"pydantic-ai-slim[bedrock]"</span>
</code></pre></div>
</div>
</div>
<div class="tabbed-control tabbed-control--prev" hidden=""><button class="tabbed-button" tabindex="-1" aria-hidden="true"></button></div><div class="tabbed-control tabbed-control--next" hidden=""><button class="tabbed-button" tabindex="-1" aria-hidden="true"></button></div></div>
<h3 id="configuration_7">Configuration</h3>
<p>To use <a href="https://aws.amazon.com/bedrock/">AWS Bedrock</a>, you'll need an AWS account with Bedrock enabled and appropriate credentials. You can use either AWS credentials directly or a pre-configured boto3 client.</p>
<p><a class="autorefs autorefs-internal" href="../api/models/bedrock/#pydantic_ai.models.bedrock.BedrockModelName"><code>BedrockModelName</code></a> contains a list of available Bedrock models, including models from Anthropic, Amazon, Cohere, Meta, and Mistral.</p>
<h3 id="environment-variables">Environment variables</h3>
<p>You can set your AWS credentials as environment variables (<a href="https://boto3.amazonaws.com/v1/documentation/api/latest/guide/configuration.html#using-environment-variables">among other options</a>:</p>
<div class="language-bash highlight"><pre id="__code_51"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_51 > code"></button><code><span class="nb">export</span><span class="w"> </span><span class="nv">AWS_ACCESS_KEY_ID</span><span class="o">=</span><span class="s1">'your-access-key'</span>
<span class="nb">export</span><span class="w"> </span><span class="nv">AWS_SECRET_ACCESS_KEY</span><span class="o">=</span><span class="s1">'your-secret-key'</span>
<span class="nb">export</span><span class="w"> </span><span class="nv">AWS_DEFAULT_REGION</span><span class="o">=</span><span class="s1">'us-east-1'</span><span class="w">  </span><span class="c1"># or your preferred region</span>
</code></pre></div>
<p>You can then use <a class="autorefs autorefs-internal" href="../api/models/bedrock/#pydantic_ai.models.bedrock.BedrockConverseModel"><code>BedrockConverseModel</code></a> by name:</p>
<div class="language-python highlight"><span class="filename">bedrock_model_by_name.py</span><pre id="__code_52"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_52 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>

<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="s1">'bedrock:anthropic.claude-3-sonnet-20240229-v1:0'</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
<p>Or initialize the model directly with just the model name:</p>
<div class="language-python highlight"><span class="filename">bedrock_model_init.py</span><pre id="__code_53"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_53 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.bedrock</span><span class="w"> </span><span class="kn">import</span> <span class="n">BedrockConverseModel</span>

<span class="n">model</span> <span class="o">=</span> <span class="n">BedrockConverseModel</span><span class="p">(</span><span class="s1">'anthropic.claude-3-sonnet-20240229-v1:0'</span><span class="p">)</span>
<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
<h3 id="provider-argument_6"><code>provider</code> argument</h3>
<p>You can provide a custom <a class="autorefs autorefs-internal" href="../api/providers/#pydantic_ai.providers.bedrock.BedrockProvider"><code>BedrockProvider</code></a> via the <a class="autorefs autorefs-internal" href="../api/models/bedrock/#pydantic_ai.models.bedrock.BedrockConverseModel.__init__"><code>provider</code> argument</a>. This is useful when you want to specify credentials directly or use a custom boto3 client:</p>
<div class="language-python highlight"><span class="filename">bedrock_model_provider.py</span><pre id="__code_54"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_54 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.bedrock</span><span class="w"> </span><span class="kn">import</span> <span class="n">BedrockConverseModel</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.providers.bedrock</span><span class="w"> </span><span class="kn">import</span> <span class="n">BedrockProvider</span>

<span class="c1"># Using AWS credentials directly</span>
<span class="n">model</span> <span class="o">=</span> <span class="n">BedrockConverseModel</span><span class="p">(</span>
    <span class="s1">'anthropic.claude-3-sonnet-20240229-v1:0'</span><span class="p">,</span>
    <span class="n">provider</span><span class="o">=</span><span class="n">BedrockProvider</span><span class="p">(</span>
        <span class="n">region_name</span><span class="o">=</span><span class="s1">'us-east-1'</span><span class="p">,</span>
        <span class="n">aws_access_key_id</span><span class="o">=</span><span class="s1">'your-access-key'</span><span class="p">,</span>
        <span class="n">aws_secret_access_key</span><span class="o">=</span><span class="s1">'your-secret-key'</span><span class="p">,</span>
    <span class="p">),</span>
<span class="p">)</span>
<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
<p>You can also pass a pre-configured boto3 client:</p>
<div class="language-python highlight"><span class="filename">bedrock_model_boto3.py</span><pre id="__code_55"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_55 > code"></button><code><span class="kn">import</span><span class="w"> </span><span class="nn">boto3</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.bedrock</span><span class="w"> </span><span class="kn">import</span> <span class="n">BedrockConverseModel</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.providers.bedrock</span><span class="w"> </span><span class="kn">import</span> <span class="n">BedrockProvider</span>

<span class="c1"># Using a pre-configured boto3 client</span>
<span class="n">bedrock_client</span> <span class="o">=</span> <span class="n">boto3</span><span class="o">.</span><span class="n">client</span><span class="p">(</span><span class="s1">'bedrock-runtime'</span><span class="p">,</span> <span class="n">region_name</span><span class="o">=</span><span class="s1">'us-east-1'</span><span class="p">)</span>
<span class="n">model</span> <span class="o">=</span> <span class="n">BedrockConverseModel</span><span class="p">(</span>
    <span class="s1">'anthropic.claude-3-sonnet-20240229-v1:0'</span><span class="p">,</span>
    <span class="n">provider</span><span class="o">=</span><span class="n">BedrockProvider</span><span class="p">(</span><span class="n">bedrock_client</span><span class="o">=</span><span class="n">bedrock_client</span><span class="p">),</span>
<span class="p">)</span>
<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
<h2 id="openai-compatible-models">OpenAI-compatible Models</h2>
<p>Many of the models are compatible with OpenAI API, and thus can be used with <a class="autorefs autorefs-internal" href="../api/models/openai/#pydantic_ai.models.openai.OpenAIModel"><code>OpenAIModel</code></a> in PydanticAI.
Before getting started, check the <a href="#openai">OpenAI</a> section for installation and configuration instructions.</p>
<p>To use another OpenAI-compatible API, you can make use of the <a class="autorefs autorefs-internal" href="../api/providers/#pydantic_ai.providers.openai.OpenAIProvider.__init__"><code>base_url</code></a>
and <a class="autorefs autorefs-internal" href="../api/providers/#pydantic_ai.providers.openai.OpenAIProvider.__init__"><code>api_key</code></a> arguments from <code>OpenAIProvider</code>:</p>
<div class="language-python highlight"><span class="filename">deepseek_model_init.py</span><pre id="__code_56"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_56 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.openai</span><span class="w"> </span><span class="kn">import</span> <span class="n">OpenAIModel</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.providers.openai</span><span class="w"> </span><span class="kn">import</span> <span class="n">OpenAIProvider</span>

<span class="hll"><span class="n">model</span> <span class="o">=</span> <span class="n">OpenAIModel</span><span class="p">(</span>
</span><span class="hll">    <span class="s1">'model_name'</span><span class="p">,</span>
</span>    <span class="n">provider</span><span class="o">=</span><span class="n">OpenAIProvider</span><span class="p">(</span>
        <span class="n">base_url</span><span class="o">=</span><span class="s1">'https://&lt;openai-compatible-api-endpoint&gt;.com'</span><span class="p">,</span> <span class="n">api_key</span><span class="o">=</span><span class="s1">'your-api-key'</span>
    <span class="p">),</span>
<span class="p">)</span>
<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
<p>You can also use the <code>provider</code> argument with a custom provider class like the <a class="autorefs autorefs-internal" href="../api/providers/#pydantic_ai.providers.deepseek.DeepSeekProvider"><code>DeepSeekProvider</code></a>:</p>
<p></p><div class="language-python highlight"><span class="filename">deepseek_model_init_provider_class.py</span><pre id="__code_57"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_57 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.openai</span><span class="w"> </span><span class="kn">import</span> <span class="n">OpenAIModel</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.providers.deepseek</span><span class="w"> </span><span class="kn">import</span> <span class="n">DeepSeekProvider</span>

<span class="n">model</span> <span class="o">=</span> <span class="n">OpenAIModel</span><span class="p">(</span>
    <span class="s1">'deepseek-chat'</span><span class="p">,</span>
    <span class="n">provider</span><span class="o">=</span><span class="n">DeepSeekProvider</span><span class="p">(</span><span class="n">api_key</span><span class="o">=</span><span class="s1">'your-deepseek-api-key'</span><span class="p">),</span>
<span class="p">)</span>
<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
You can also customize any provider with a custom <code>http_client</code>:
<div class="language-python highlight"><span class="filename">deepseek_model_init_provider_custom.py</span><pre id="__code_58"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_58 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">httpx</span><span class="w"> </span><span class="kn">import</span> <span class="n">AsyncClient</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.openai</span><span class="w"> </span><span class="kn">import</span> <span class="n">OpenAIModel</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.providers.deepseek</span><span class="w"> </span><span class="kn">import</span> <span class="n">DeepSeekProvider</span>

<span class="n">custom_http_client</span> <span class="o">=</span> <span class="n">AsyncClient</span><span class="p">(</span><span class="n">timeout</span><span class="o">=</span><span class="mi">30</span><span class="p">)</span>
<span class="n">model</span> <span class="o">=</span> <span class="n">OpenAIModel</span><span class="p">(</span>
    <span class="s1">'deepseek-chat'</span><span class="p">,</span>
    <span class="n">provider</span><span class="o">=</span><span class="n">DeepSeekProvider</span><span class="p">(</span>
        <span class="n">api_key</span><span class="o">=</span><span class="s1">'your-deepseek-api-key'</span><span class="p">,</span> <span class="n">http_client</span><span class="o">=</span><span class="n">custom_http_client</span>
    <span class="p">),</span>
<span class="p">)</span>
<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div><p></p>
<h3 id="ollama">Ollama</h3>
<p>To use <a href="https://ollama.com/">Ollama</a>, you must first download the Ollama client, and then download a model using the <a href="https://ollama.com/library">Ollama model library</a>.</p>
<p>You must also ensure the Ollama server is running when trying to make requests to it. For more information, please see the <a href="https://github.com/ollama/ollama/tree/main/docs">Ollama documentation</a>.</p>
<h4 id="example-local-usage">Example local usage</h4>
<p>With <code>ollama</code> installed, you can run the server with the model you want to use:</p>
<div class="language-bash highlight"><span class="filename">terminal-run-ollama</span><pre id="__code_59"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_59 > code"></button><code>ollama<span class="w"> </span>run<span class="w"> </span>llama3.2
</code></pre></div>
<p>(this will pull the <code>llama3.2</code> model if you don't already have it downloaded)</p>
<p>Then run your code, here's a minimal example:</p>
<div class="language-python highlight"><span class="filename">ollama_example.py</span><pre id="__code_60"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_60 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic</span><span class="w"> </span><span class="kn">import</span> <span class="n">BaseModel</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.openai</span><span class="w"> </span><span class="kn">import</span> <span class="n">OpenAIModel</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.providers.openai</span><span class="w"> </span><span class="kn">import</span> <span class="n">OpenAIProvider</span>


<span class="k">class</span><span class="w"> </span><span class="nc">CityLocation</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">city</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">country</span><span class="p">:</span> <span class="nb">str</span>


<span class="n">ollama_model</span> <span class="o">=</span> <span class="n">OpenAIModel</span><span class="p">(</span>
    <span class="n">model_name</span><span class="o">=</span><span class="s1">'llama3.2'</span><span class="p">,</span> <span class="n">provider</span><span class="o">=</span><span class="n">OpenAIProvider</span><span class="p">(</span><span class="n">base_url</span><span class="o">=</span><span class="s1">'http://localhost:11434/v1'</span><span class="p">)</span>
<span class="p">)</span>
<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">ollama_model</span><span class="p">,</span> <span class="n">result_type</span><span class="o">=</span><span class="n">CityLocation</span><span class="p">)</span>

<span class="n">result</span> <span class="o">=</span> <span class="n">agent</span><span class="o">.</span><span class="n">run_sync</span><span class="p">(</span><span class="s1">'Where were the olympics held in 2012?'</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>
<span class="c1">#&gt; city='London' country='United Kingdom'</span>
<span class="nb">print</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">usage</span><span class="p">())</span>
<span class="sd">"""</span>
<span class="sd">Usage(requests=1, request_tokens=57, response_tokens=8, total_tokens=65, details=None)</span>
<span class="sd">"""</span>
</code></pre></div>
<h4 id="example-using-a-remote-server">Example using a remote server</h4>
<div class="language-python highlight"><span class="filename">ollama_example_with_remote_server.py</span><pre id="__code_61"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_61 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic</span><span class="w"> </span><span class="kn">import</span> <span class="n">BaseModel</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.openai</span><span class="w"> </span><span class="kn">import</span> <span class="n">OpenAIModel</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.providers.openai</span><span class="w"> </span><span class="kn">import</span> <span class="n">OpenAIProvider</span>

<span class="n">ollama_model</span> <span class="o">=</span> <span class="n">OpenAIModel</span><span class="p">(</span>
    <span class="n">model_name</span><span class="o">=</span><span class="s1">'qwen2.5-coder:7b'</span><span class="p">,</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 322px; --md-tooltip-y: 153px; --md-tooltip-0: -16px;"><div class="md-tooltip" id="__code_61_annotation_1" role="tooltip"><div class="md-tooltip__inner md-typeset">The name of the model running on the remote server</div></div><a href="#__code_61_annotation_1" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="1"></span></a></aside></span>
    <span class="n">provider</span><span class="o">=</span><span class="n">OpenAIProvider</span><span class="p">(</span><span class="n">base_url</span><span class="o">=</span><span class="s1">'http://192.168.1.74:11434/v1'</span><span class="p">),</span>  <span class="c1"><aside class="md-annotation" tabindex="0" style="--md-tooltip-x: 608px; --md-tooltip-y: 172px; --md-tooltip-0: -16px;"><div class="md-tooltip" id="__code_61_annotation_2" role="tooltip"><div class="md-tooltip__inner md-typeset">The url of the remote server</div></div><a href="#__code_61_annotation_2" class="md-annotation__index" tabindex="-1"><span data-md-annotation-id="2"></span></a></aside></span>
<span class="p">)</span>


<span class="k">class</span><span class="w"> </span><span class="nc">CityLocation</span><span class="p">(</span><span class="n">BaseModel</span><span class="p">):</span>
    <span class="n">city</span><span class="p">:</span> <span class="nb">str</span>
    <span class="n">country</span><span class="p">:</span> <span class="nb">str</span>


<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">model</span><span class="o">=</span><span class="n">ollama_model</span><span class="p">,</span> <span class="n">result_type</span><span class="o">=</span><span class="n">CityLocation</span><span class="p">)</span>

<span class="n">result</span> <span class="o">=</span> <span class="n">agent</span><span class="o">.</span><span class="n">run_sync</span><span class="p">(</span><span class="s1">'Where were the olympics held in 2012?'</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>
<span class="c1">#&gt; city='London' country='United Kingdom'</span>
<span class="nb">print</span><span class="p">(</span><span class="n">result</span><span class="o">.</span><span class="n">usage</span><span class="p">())</span>
<span class="sd">"""</span>
<span class="sd">Usage(requests=1, request_tokens=57, response_tokens=8, total_tokens=65, details=None)</span>
<span class="sd">"""</span>
</code></pre></div>
<ol hidden="">
<li></li>
<li></li>
</ol>
<h3 id="azure-ai-foundry">Azure AI Foundry</h3>
<p>If you want to use <a href="https://ai.azure.com/">Azure AI Foundry</a> as your provider, you can do so by using the
<a class="autorefs autorefs-internal" href="../api/providers/#pydantic_ai.providers.azure.AzureProvider"><code>AzureProvider</code></a> class.</p>
<div class="language-python highlight"><span class="filename">azure_provider_example.py</span><pre id="__code_62"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_62 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.openai</span><span class="w"> </span><span class="kn">import</span> <span class="n">OpenAIModel</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.providers.azure</span><span class="w"> </span><span class="kn">import</span> <span class="n">AzureProvider</span>

<span class="n">model</span> <span class="o">=</span> <span class="n">OpenAIModel</span><span class="p">(</span>
    <span class="s1">'gpt-4o'</span><span class="p">,</span>
    <span class="n">provider</span><span class="o">=</span><span class="n">AzureProvider</span><span class="p">(</span>
        <span class="n">azure_endpoint</span><span class="o">=</span><span class="s1">'your-azure-endpoint'</span><span class="p">,</span>
        <span class="n">api_version</span><span class="o">=</span><span class="s1">'your-api-version'</span><span class="p">,</span>
        <span class="n">api_key</span><span class="o">=</span><span class="s1">'your-api-key'</span><span class="p">,</span>
    <span class="p">),</span>
<span class="p">)</span>
<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
<h3 id="openrouter">OpenRouter</h3>
<p>To use <a href="https://openrouter.ai">OpenRouter</a>, first create an API key at <a href="https://openrouter.ai/keys">openrouter.ai/keys</a>.</p>
<p>Once you have the API key, you can use it with the <a class="autorefs autorefs-internal" href="../api/providers/#pydantic_ai.providers.openai.OpenAIProvider"><code>OpenAIProvider</code></a>:</p>
<div class="language-python highlight"><span class="filename">openrouter_model_init.py</span><pre id="__code_63"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_63 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.openai</span><span class="w"> </span><span class="kn">import</span> <span class="n">OpenAIModel</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.providers.openai</span><span class="w"> </span><span class="kn">import</span> <span class="n">OpenAIProvider</span>

<span class="n">model</span> <span class="o">=</span> <span class="n">OpenAIModel</span><span class="p">(</span>
    <span class="s1">'anthropic/claude-3.5-sonnet'</span><span class="p">,</span>
    <span class="n">provider</span><span class="o">=</span><span class="n">OpenAIProvider</span><span class="p">(</span>
        <span class="n">base_url</span><span class="o">=</span><span class="s1">'https://openrouter.ai/api/v1'</span><span class="p">,</span>
        <span class="n">api_key</span><span class="o">=</span><span class="s1">'your-openrouter-api-key'</span><span class="p">,</span>
    <span class="p">),</span>
<span class="p">)</span>
<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
<h3 id="grok-xai">Grok (xAI)</h3>
<p>Go to <a href="https://console.x.ai/">xAI API Console</a> and create an API key.
Once you have the API key, you can use it with the <a class="autorefs autorefs-internal" href="../api/providers/#pydantic_ai.providers.openai.OpenAIProvider"><code>OpenAIProvider</code></a>:</p>
<div class="language-python highlight"><span class="filename">grok_model_init.py</span><pre id="__code_64"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_64 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.openai</span><span class="w"> </span><span class="kn">import</span> <span class="n">OpenAIModel</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.providers.openai</span><span class="w"> </span><span class="kn">import</span> <span class="n">OpenAIProvider</span>

<span class="n">model</span> <span class="o">=</span> <span class="n">OpenAIModel</span><span class="p">(</span>
    <span class="s1">'grok-2-1212'</span><span class="p">,</span>
    <span class="n">provider</span><span class="o">=</span><span class="n">OpenAIProvider</span><span class="p">(</span><span class="n">base_url</span><span class="o">=</span><span class="s1">'https://api.x.ai/v1'</span><span class="p">,</span> <span class="n">api_key</span><span class="o">=</span><span class="s1">'your-xai-api-key'</span><span class="p">),</span>
<span class="p">)</span>
<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
<h3 id="perplexity">Perplexity</h3>
<p>Follow the Perplexity <a href="https://docs.perplexity.ai/guides/getting-started">getting started</a>
guide to create an API key. Then, you can query the Perplexity API with the following:</p>
<div class="language-py highlight"><span class="filename">perplexity_model_init.py</span><pre id="__code_65"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_65 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.openai</span><span class="w"> </span><span class="kn">import</span> <span class="n">OpenAIModel</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.providers.openai</span><span class="w"> </span><span class="kn">import</span> <span class="n">OpenAIProvider</span>

<span class="n">model</span> <span class="o">=</span> <span class="n">OpenAIModel</span><span class="p">(</span>
    <span class="s1">'sonar-pro'</span><span class="p">,</span>
    <span class="n">provider</span><span class="o">=</span><span class="n">OpenAIProvider</span><span class="p">(</span>
        <span class="n">base_url</span><span class="o">=</span><span class="s1">'https://api.perplexity.ai'</span><span class="p">,</span>
        <span class="n">api_key</span><span class="o">=</span><span class="s1">'your-perplexity-api-key'</span><span class="p">,</span>
    <span class="p">),</span>
<span class="p">)</span>
<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
<h3 id="fireworks-ai">Fireworks AI</h3>
<p>Go to <a href="https://fireworks.ai/">Fireworks.AI</a> and create an API key in your account settings.
Once you have the API key, you can use it with the <a class="autorefs autorefs-internal" href="../api/providers/#pydantic_ai.providers.openai.OpenAIProvider"><code>OpenAIProvider</code></a>:</p>
<div class="language-python highlight"><span class="filename">fireworks_model_init.py</span><pre id="__code_66"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_66 > code"></button><code tabindex="0"><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.openai</span><span class="w"> </span><span class="kn">import</span> <span class="n">OpenAIModel</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.providers.openai</span><span class="w"> </span><span class="kn">import</span> <span class="n">OpenAIProvider</span>

<span class="n">model</span> <span class="o">=</span> <span class="n">OpenAIModel</span><span class="p">(</span>
    <span class="s1">'accounts/fireworks/models/qwq-32b'</span><span class="p">,</span>  <span class="c1"># model library available at https://fireworks.ai/models</span>
    <span class="n">provider</span><span class="o">=</span><span class="n">OpenAIProvider</span><span class="p">(</span>
        <span class="n">base_url</span><span class="o">=</span><span class="s1">'https://api.fireworks.ai/inference/v1'</span><span class="p">,</span>
        <span class="n">api_key</span><span class="o">=</span><span class="s1">'your-fireworks-api-key'</span><span class="p">,</span>
    <span class="p">),</span>
<span class="p">)</span>
<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
<h3 id="together-ai">Together AI</h3>
<p>Go to <a href="https://www.together.ai/">Together.ai</a> and create an API key in your account settings.
Once you have the API key, you can use it with the <a class="autorefs autorefs-internal" href="../api/providers/#pydantic_ai.providers.openai.OpenAIProvider"><code>OpenAIProvider</code></a>:</p>
<div class="language-python highlight"><span class="filename">together_model_init.py</span><pre id="__code_67"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_67 > code"></button><code tabindex="0"><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.openai</span><span class="w"> </span><span class="kn">import</span> <span class="n">OpenAIModel</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.providers.openai</span><span class="w"> </span><span class="kn">import</span> <span class="n">OpenAIProvider</span>

<span class="n">model</span> <span class="o">=</span> <span class="n">OpenAIModel</span><span class="p">(</span>
    <span class="s1">'meta-llama/Llama-3.3-70B-Instruct-Turbo-Free'</span><span class="p">,</span>  <span class="c1"># model library available at https://www.together.ai/models</span>
    <span class="n">provider</span><span class="o">=</span><span class="n">OpenAIProvider</span><span class="p">(</span>
        <span class="n">base_url</span><span class="o">=</span><span class="s1">'https://api.together.xyz/v1'</span><span class="p">,</span>
        <span class="n">api_key</span><span class="o">=</span><span class="s1">'your-together-api-key'</span><span class="p">,</span>
    <span class="p">),</span>
<span class="p">)</span>
<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">model</span><span class="p">)</span>
<span class="o">...</span>
</code></pre></div>
<h2 id="implementing-custom-models">Implementing Custom Models</h2>
<p>To implement support for models not already supported, you will need to subclass the <a class="autorefs autorefs-internal" href="../api/models/base/#pydantic_ai.models.Model"><code>Model</code></a> abstract base class.</p>
<p>For streaming, you'll also need to implement the following abstract base class:</p>
<ul>
<li><a class="autorefs autorefs-internal" href="../api/models/base/#pydantic_ai.models.StreamedResponse"><code>StreamedResponse</code></a></li>
</ul>
<p>The best place to start is to review the source code for existing implementations, e.g. <a href="https://github.com/pydantic/pydantic-ai/blob/main/pydantic_ai_slim/pydantic_ai/models/openai.py"><code>OpenAIModel</code></a>.</p>
<p>For details on when we'll accept contributions adding new models to PydanticAI, see the <a href="../contributing/#new-model-rules">contributing guidelines</a>.</p>
<h2 id="fallback">Fallback</h2>
<p>You can use <a class="autorefs autorefs-internal" href="../api/models/fallback/#pydantic_ai.models.fallback.FallbackModel"><code>FallbackModel</code></a> to attempt multiple models
in sequence until one returns a successful result. Under the hood, PydanticAI automatically switches
from one model to the next if the current model returns a 4xx or 5xx status code.</p>
<p>In the following example, the agent first makes a request to the OpenAI model (which fails due to an invalid API key),
and then falls back to the Anthropic model.</p>
<div class="language-python highlight"><span class="filename">fallback_model.py</span><pre id="__code_68"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_68 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.anthropic</span><span class="w"> </span><span class="kn">import</span> <span class="n">AnthropicModel</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.fallback</span><span class="w"> </span><span class="kn">import</span> <span class="n">FallbackModel</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.openai</span><span class="w"> </span><span class="kn">import</span> <span class="n">OpenAIModel</span>

<span class="n">openai_model</span> <span class="o">=</span> <span class="n">OpenAIModel</span><span class="p">(</span><span class="s1">'gpt-4o'</span><span class="p">)</span>
<span class="n">anthropic_model</span> <span class="o">=</span> <span class="n">AnthropicModel</span><span class="p">(</span><span class="s1">'claude-3-5-sonnet-latest'</span><span class="p">)</span>
<span class="n">fallback_model</span> <span class="o">=</span> <span class="n">FallbackModel</span><span class="p">(</span><span class="n">openai_model</span><span class="p">,</span> <span class="n">anthropic_model</span><span class="p">)</span>

<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">fallback_model</span><span class="p">)</span>
<span class="n">response</span> <span class="o">=</span> <span class="n">agent</span><span class="o">.</span><span class="n">run_sync</span><span class="p">(</span><span class="s1">'What is the capital of France?'</span><span class="p">)</span>
<span class="nb">print</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">data</span><span class="p">)</span>
<span class="c1">#&gt; Paris</span>

<span class="nb">print</span><span class="p">(</span><span class="n">response</span><span class="o">.</span><span class="n">all_messages</span><span class="p">())</span>
<span class="sd">"""</span>
<span class="sd">[</span>
<span class="sd">    ModelRequest(</span>
<span class="sd">        parts=[</span>
<span class="sd">            UserPromptPart(</span>
<span class="sd">                content='What is the capital of France?',</span>
<span class="sd">                timestamp=datetime.datetime(...),</span>
<span class="sd">                part_kind='user-prompt',</span>
<span class="sd">            )</span>
<span class="sd">        ],</span>
<span class="sd">        kind='request',</span>
<span class="sd">    ),</span>
<span class="sd">    ModelResponse(</span>
<span class="sd">        parts=[TextPart(content='Paris', part_kind='text')],</span>
<span class="sd">        model_name='claude-3-5-sonnet-latest',</span>
<span class="sd">        timestamp=datetime.datetime(...),</span>
<span class="sd">        kind='response',</span>
<span class="sd">    ),</span>
<span class="sd">]</span>
<span class="sd">"""</span>
</code></pre></div>
<p>The <code>ModelResponse</code> message above indicates in the <code>model_name</code> field that the result was returned by the Anthropic model, which is the second model specified in the <code>FallbackModel</code>.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>Each model's options should be configured individually. For example, <code>base_url</code>, <code>api_key</code>, and custom clients should be set on each model itself, not on the <code>FallbackModel</code>.</p>
</div>
<p>In this next example, we demonstrate the exception-handling capabilities of <code>FallbackModel</code>.
If all models fail, a <a class="autorefs autorefs-internal" href="../api/exceptions/#pydantic_ai.exceptions.FallbackExceptionGroup"><code>FallbackExceptionGroup</code></a> is raised, which
contains all the exceptions encountered during the <code>run</code> execution.</p>
<div class="tabbed-set tabbed-alternate" data-tabs="8:2"><input checked="checked" id="__tabbed_8_1" name="__tabbed_8" type="radio"><input id="__tabbed_8_2" name="__tabbed_8" type="radio"><div class="tabbed-labels tabbed-labels--linked"><label for="__tabbed_8_1"><a href="#__tabbed_8_1" tabindex="-1">Python &gt;=3.11</a></label><label for="__tabbed_8_2"><a href="#__tabbed_8_2" tabindex="-1">Python &lt;3.11</a></label></div>
<div class="tabbed-content">
<div class="tabbed-block">
<div class="language-python highlight"><span class="filename">fallback_model_failure.py</span><pre id="__code_69"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_69 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.exceptions</span><span class="w"> </span><span class="kn">import</span> <span class="n">ModelHTTPError</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.anthropic</span><span class="w"> </span><span class="kn">import</span> <span class="n">AnthropicModel</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.fallback</span><span class="w"> </span><span class="kn">import</span> <span class="n">FallbackModel</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.openai</span><span class="w"> </span><span class="kn">import</span> <span class="n">OpenAIModel</span>

<span class="n">openai_model</span> <span class="o">=</span> <span class="n">OpenAIModel</span><span class="p">(</span><span class="s1">'gpt-4o'</span><span class="p">)</span>
<span class="n">anthropic_model</span> <span class="o">=</span> <span class="n">AnthropicModel</span><span class="p">(</span><span class="s1">'claude-3-5-sonnet-latest'</span><span class="p">)</span>
<span class="n">fallback_model</span> <span class="o">=</span> <span class="n">FallbackModel</span><span class="p">(</span><span class="n">openai_model</span><span class="p">,</span> <span class="n">anthropic_model</span><span class="p">)</span>

<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">fallback_model</span><span class="p">)</span>
<span class="k">try</span><span class="p">:</span>
    <span class="n">response</span> <span class="o">=</span> <span class="n">agent</span><span class="o">.</span><span class="n">run_sync</span><span class="p">(</span><span class="s1">'What is the capital of France?'</span><span class="p">)</span>
<span class="k">except</span><span class="o">*</span> <span class="n">ModelHTTPError</span> <span class="k">as</span> <span class="n">exc_group</span><span class="p">:</span>
    <span class="k">for</span> <span class="n">exc</span> <span class="ow">in</span> <span class="n">exc_group</span><span class="o">.</span><span class="n">exceptions</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">exc</span><span class="p">)</span>
</code></pre></div>
</div>
<div class="tabbed-block">
<p>Since <a href="https://docs.python.org/3/reference/compound_stmts.html#except-star"><code>except*</code></a> is only supported
in Python 3.11+, we use the <a href="https://github.com/agronholm/exceptiongroup"><code>exceptiongroup</code></a> backport
package for earlier Python versions:</p>
<div class="language-python highlight"><span class="filename">fallback_model_failure.py</span><pre id="__code_70"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_70 > code"></button><code><span class="kn">from</span><span class="w"> </span><span class="nn">exceptiongroup</span><span class="w"> </span><span class="kn">import</span> <span class="n">catch</span>

<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">Agent</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.exceptions</span><span class="w"> </span><span class="kn">import</span> <span class="n">ModelHTTPError</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.anthropic</span><span class="w"> </span><span class="kn">import</span> <span class="n">AnthropicModel</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.fallback</span><span class="w"> </span><span class="kn">import</span> <span class="n">FallbackModel</span>
<span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai.models.openai</span><span class="w"> </span><span class="kn">import</span> <span class="n">OpenAIModel</span>


<span class="k">def</span><span class="w"> </span><span class="nf">model_status_error_handler</span><span class="p">(</span><span class="n">exc_group</span><span class="p">:</span> <span class="n">BaseExceptionGroup</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
    <span class="k">for</span> <span class="n">exc</span> <span class="ow">in</span> <span class="n">exc_group</span><span class="o">.</span><span class="n">exceptions</span><span class="p">:</span>
        <span class="nb">print</span><span class="p">(</span><span class="n">exc</span><span class="p">)</span>


<span class="n">openai_model</span> <span class="o">=</span> <span class="n">OpenAIModel</span><span class="p">(</span><span class="s1">'gpt-4o'</span><span class="p">)</span>
<span class="n">anthropic_model</span> <span class="o">=</span> <span class="n">AnthropicModel</span><span class="p">(</span><span class="s1">'claude-3-5-sonnet-latest'</span><span class="p">)</span>
<span class="n">fallback_model</span> <span class="o">=</span> <span class="n">FallbackModel</span><span class="p">(</span><span class="n">openai_model</span><span class="p">,</span> <span class="n">anthropic_model</span><span class="p">)</span>

<span class="n">agent</span> <span class="o">=</span> <span class="n">Agent</span><span class="p">(</span><span class="n">fallback_model</span><span class="p">)</span>
<span class="k">with</span> <span class="n">catch</span><span class="p">({</span><span class="n">ModelHTTPError</span><span class="p">:</span> <span class="n">model_status_error_handler</span><span class="p">}):</span>
    <span class="n">response</span> <span class="o">=</span> <span class="n">agent</span><span class="o">.</span><span class="n">run_sync</span><span class="p">(</span><span class="s1">'What is the capital of France?'</span><span class="p">)</span>
</code></pre></div>
</div>
</div>
<div class="tabbed-control tabbed-control--prev" hidden=""><button class="tabbed-button" tabindex="-1" aria-hidden="true"></button></div><div class="tabbed-control tabbed-control--next" hidden=""><button class="tabbed-button" tabindex="-1" aria-hidden="true"></button></div></div>
<p>By default, the <code>FallbackModel</code> only moves on to the next model if the current model raises a
<a class="autorefs autorefs-internal" href="../api/exceptions/#pydantic_ai.exceptions.ModelHTTPError"><code>ModelHTTPError</code></a>. You can customize this behavior by
passing a custom <code>fallback_on</code> argument to the <code>FallbackModel</code> constructor.</p>







  
  






                
              </article>
            </div>
          
          
  <script>var tabs=__md_get("__tabs");if(Array.isArray(tabs))e:for(var set of document.querySelectorAll(".tabbed-set")){var labels=set.querySelector(".tabbed-labels");for(var tab of tabs)for(var label of labels.getElementsByTagName("label"))if(label.innerText.trim()===tab){var input=document.getElementById(label.htmlFor);input.checked=!0;continue e}}</script>

<script>var target=document.getElementById(location.hash.slice(1));target&&target.name&&(target.checked=target.name.startsWith("__tabbed_"))</script>
        </div>
        
      </main>
      
        <footer class="md-footer">
  
  <div class="md-footer-meta md-typeset">
    <div class="md-footer-meta__inner md-grid">
      <div class="md-copyright">
  
    <div class="md-copyright__highlight">
      © Pydantic Services Inc. 2024 to present
    </div>
  
  
</div>
      
    </div>
  </div>
</footer>
      
    </div>
    <div class="md-dialog" data-md-component="dialog">
      <div class="md-dialog__inner md-typeset"></div>
    </div>
    
    
    <script id="__config" type="application/json">{"base": "..", "features": ["search.suggest", "search.highlight", "content.tabs.link", "content.code.annotate", "content.code.copy", "content.code.select", "navigation.path", "navigation.indexes", "navigation.sections", "navigation.tracking", "toc.follow"], "search": "../assets/javascripts/workers/search.f8cc74c7.min.js", "translations": {"clipboard.copied": "Copied to clipboard", "clipboard.copy": "Copy to clipboard", "search.result.more.one": "1 more on this page", "search.result.more.other": "# more on this page", "search.result.none": "No matching documents", "search.result.one": "1 matching document", "search.result.other": "# matching documents", "search.result.placeholder": "Type to start searching", "search.result.term.missing": "Missing", "select.version": "Select version"}}</script>
    
    
      <script src="../assets/javascripts/bundle.f1b6f286.min.js"></script>
      
        <script src="/flarelytics/client.js"></script>
      
        <script src="https://cdn.jsdelivr.net/npm/algoliasearch@5.20.0/dist/lite/builds/browser.umd.js"></script>
      
        <script src="https://cdn.jsdelivr.net/npm/instantsearch.js@4.77.3/dist/instantsearch.production.min.js"></script>
      
        <script src="/javascripts/algolia-search.js"></script>
      
    
  <script id="init-glightbox">const lightbox = GLightbox({"touchNavigation": true, "loop": false, "zoomable": true, "draggable": true, "openEffect": "zoom", "closeEffect": "zoom", "slideEffect": "slide"});
document$.subscribe(() => { lightbox.reload() });
</script>
</body></html>