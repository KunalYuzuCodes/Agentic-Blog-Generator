<!DOCTYPE html><html lang="en" class="js-focus-visible js" data-js-focus-visible=""><head>
    
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width,initial-scale=1">
      
        <meta name="description" content="Agent Framework / shim to use Pydantic with LLMs">
      
      
      
        <link rel="canonical" href="https://ai.pydantic.dev/api/models/base/">
      
      
        <link rel="prev" href="../../format_as_xml/">
      
      
        <link rel="next" href="../openai/">
      
      
      <link rel="icon" href="../../../favicon.ico">
      <meta name="generator" content="mkdocs-1.6.1, mkdocs-material-9.6.5">
    
    
      
        <title>pydantic_ai.models - PydanticAI</title>
      
    
    
      <link rel="stylesheet" href="../../../assets/stylesheets/main.8608ea7d.min.css">
      
        
        <link rel="stylesheet" href="../../../assets/stylesheets/palette.06af60db.min.css">
      
      


    
    
      
    
    
      
        
        
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300i,400,400i,700,700i%7CRoboto+Mono:400,400i,700,700i&amp;display=fallback">
        <style>:root{--md-text-font:"Roboto";--md-code-font:"Roboto Mono"}</style>
      
    
    
      <link rel="stylesheet" href="../../../assets/_mkdocstrings.css">
    
      <link rel="stylesheet" href="../../../extra/tweaks.css">
    
    <script>__md_scope=new URL("../../..",location),__md_hash=e=>[...e].reduce(((e,_)=>(e<<5)-e+_.charCodeAt(0)),0),__md_get=(e,_=localStorage,t=__md_scope)=>JSON.parse(_.getItem(t.pathname+"."+e)),__md_set=(e,_,t=localStorage,a=__md_scope)=>{try{t.setItem(a.pathname+"."+e,JSON.stringify(_))}catch(e){}}</script>
    
      

    
    
      
        <meta property="og:type" content="website">
      
        <meta property="og:title" content="pydantic_ai.models - PydanticAI">
      
        <meta property="og:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta property="og:image" content="https://ai.pydantic.dev/assets/images/social/api/models/base.png">
      
        <meta property="og:image:type" content="image/png">
      
        <meta property="og:image:width" content="1200">
      
        <meta property="og:image:height" content="630">
      
        <meta property="og:url" content="https://ai.pydantic.dev/api/models/base/">
      
        <meta name="twitter:card" content="summary_large_image">
      
        <meta name="twitter:title" content="pydantic_ai.models - PydanticAI">
      
        <meta name="twitter:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta name="twitter:image" content="https://ai.pydantic.dev/assets/images/social/api/models/base.png">
      
    
    
   <link href="../../../assets/stylesheets/glightbox.min.css" rel="stylesheet"><style>
    html.glightbox-open { overflow: initial; height: 100%; }
    .gslide-title { margin-top: 0px; user-select: text; }
    .gslide-desc { color: #666; user-select: text; }
    .gslide-image img { background: white; }
    .gscrollbar-fixer { padding-right: 15px; }
    .gdesc-inner { font-size: 0.75rem; }
    body[data-md-color-scheme="slate"] .gdesc-inner { background: var(--md-default-bg-color);}
    body[data-md-color-scheme="slate"] .gslide-title { color: var(--md-default-fg-color);}
    body[data-md-color-scheme="slate"] .gslide-desc { color: var(--md-default-fg-color);}</style> <script src="../../../assets/javascripts/glightbox.min.js"></script><meta name="theme-color" content="#e92063"><meta name="color-scheme" content="light"></head>
  
  
    
    
      
    
    
    
    
    <body dir="ltr" data-md-color-scheme="default" data-md-color-primary="pink" data-md-color-accent="pink" data-md-color-media="(prefers-color-scheme)">
  
    
    <input class="md-toggle" data-md-toggle="drawer" type="checkbox" id="__drawer" autocomplete="off">
    <input class="md-toggle" data-md-toggle="search" type="checkbox" id="__search" autocomplete="off">
    <label class="md-overlay" for="__drawer"></label>
    <div data-md-component="skip">
      
        
        <a href="#pydantic_aimodels" class="md-skip">
          Skip to content
        </a>
      
    </div>
    <div data-md-component="announce">
      
    </div>
    
    
      

  

<header class="md-header md-header--shadow" data-md-component="header">
  <nav class="md-header__inner md-grid" aria-label="Header">
    <a href="../../.." title="PydanticAI" class="md-header__button md-logo" aria-label="PydanticAI" data-md-component="logo">
      
  <img src="../../../img/logo-white.svg" alt="logo">

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
            
              pydantic_ai.models
            
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
    <a href="../../.." title="PydanticAI" class="md-nav__button md-logo" aria-label="PydanticAI" data-md-component="logo">
      
  <img src="../../../img/logo-white.svg" alt="logo">

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
      <a href="../../.." class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Introduction
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../install/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Installation
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../help/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Getting Help
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../contributing/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Contributing
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../troubleshooting/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Troubleshooting
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    
    
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
      
        
        
      
    
    
    <li class="md-nav__item md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_6">
        
          
          <label class="md-nav__link" for="__nav_6" id="__nav_6_label" tabindex="">
            
  
  <span class="md-ellipsis">
    Documentation
    
  </span>
  

            <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_6_label" aria-expanded="false">
          <label class="md-nav__title" for="__nav_6">
            <span class="md-nav__icon md-icon"></span>
            Documentation
          </label>
          <ul class="md-nav__list">
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../agents/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Agents
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../models/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Models
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../dependencies/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Dependencies
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Function Tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../common-tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Common Tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../results/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Results
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../message-history/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Messages and chat history
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../testing/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Unit testing
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../logfire/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Debugging and Monitoring
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../multi-agent-applications/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Multi-agent Applications
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Graphs
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../evals/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Evals
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../input/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Image, Audio &amp; Document Input
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    
    
      
        
          
        
      
        
      
        
      
        
      
    
    
      
    
    
    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_6_14">
        
          
          
          <div class="md-nav__link md-nav__container">
            <a href="../../../mcp/" class="md-nav__link ">
              
  
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
      <a href="../../../mcp/client/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Client
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../mcp/server/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Server
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../mcp/run-python/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    MCP Run Python
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../cli/" class="md-nav__link">
        
  
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
            <a href="../../../examples/" class="md-nav__link ">
              
  
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
      <a href="../../../examples/pydantic-model/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Pydantic Model
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/weather-agent/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Weather agent
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/bank-support/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Bank support
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/sql-gen/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    SQL Generation
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/flight-booking/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Flight booking
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/rag/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    RAG
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/stream-markdown/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Stream markdown
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/stream-whales/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Stream whales
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/chat-app/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Chat App with FastAPI
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../../examples/question-graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Question Graph
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

    
      
      
  
  
    
  
  
  
    
    
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
        
      
    
    
      
        
        
      
    
    
    <li class="md-nav__item md-nav__item--active md-nav__item--section md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_8" checked="">
        
          
          <label class="md-nav__link" for="__nav_8" id="__nav_8_label" tabindex="">
            
  
  <span class="md-ellipsis">
    API Reference
    
  </span>
  

            <span class="md-nav__icon md-icon"></span>
          </label>
        
        <nav class="md-nav" data-md-level="1" aria-labelledby="__nav_8_label" aria-expanded="true">
          <label class="md-nav__title" for="__nav_8">
            <span class="md-nav__icon md-icon"></span>
            API Reference
          </label>
          <ul class="md-nav__list">
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../agent/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.agent
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../common_tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.common_tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../result/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.result
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../messages/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.messages
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../exceptions/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.exceptions
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../settings/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.settings
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../usage/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.usage
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../mcp/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.mcp
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../format_as_xml/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.format_as_xml
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
    
  
  
  
    <li class="md-nav__item md-nav__item--active">
      
      <input class="md-nav__toggle md-toggle" type="checkbox" id="__toc">
      
      
        
      
      
        <label class="md-nav__link md-nav__link--active" for="__toc">
          
  
  <span class="md-ellipsis">
    pydantic_ai.models
    
  </span>
  

          <span class="md-nav__icon md-icon"></span>
        </label>
      
      <a href="./" class="md-nav__link md-nav__link--active">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models
    
  </span>
  

      </a>
      
        

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
    
  
  
    <label class="md-nav__title" for="__toc">
      <span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
    <ul class="md-nav__list" data-md-component="toc">
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.models" class="md-nav__link">
    <span class="md-ellipsis">
      models
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.models.KnownModelName" class="md-nav__link">
    <span class="md-ellipsis">
      KnownModelName
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.models.ModelRequestParameters" class="md-nav__link">
    <span class="md-ellipsis">
      ModelRequestParameters
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.models.Model" class="md-nav__link">
    <span class="md-ellipsis">
      Model
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Model">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.Model.request" class="md-nav__link">
    <span class="md-ellipsis">
      request
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.Model.request_stream" class="md-nav__link">
    <span class="md-ellipsis">
      request_stream
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.Model.model_name" class="md-nav__link">
    <span class="md-ellipsis">
      model_name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.Model.system" class="md-nav__link">
    <span class="md-ellipsis">
      system
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.Model.base_url" class="md-nav__link">
    <span class="md-ellipsis">
      base_url
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.models.StreamedResponse" class="md-nav__link">
    <span class="md-ellipsis">
      StreamedResponse
    </span>
  </a>
  
    <nav class="md-nav" aria-label="StreamedResponse">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.StreamedResponse.__aiter__" class="md-nav__link">
    <span class="md-ellipsis">
      __aiter__
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.StreamedResponse.get" class="md-nav__link">
    <span class="md-ellipsis">
      get
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.StreamedResponse.usage" class="md-nav__link">
    <span class="md-ellipsis">
      usage
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.StreamedResponse.model_name" class="md-nav__link">
    <span class="md-ellipsis">
      model_name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.StreamedResponse.timestamp" class="md-nav__link">
    <span class="md-ellipsis">
      timestamp
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.models.ALLOW_MODEL_REQUESTS" class="md-nav__link">
    <span class="md-ellipsis">
      ALLOW_MODEL_REQUESTS
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.models.check_allow_model_requests" class="md-nav__link">
    <span class="md-ellipsis">
      check_allow_model_requests
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.models.override_allow_model_requests" class="md-nav__link">
    <span class="md-ellipsis">
      override_allow_model_requests
    </span>
  </a>
  
</li>
      
    </ul>
  
</nav>
      
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../openai/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.openai
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../anthropic/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.anthropic
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../bedrock/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.bedrock
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../cohere/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.cohere
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../gemini/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.gemini
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../groq/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.groq
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../instrumented/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.instrumented
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../mistral/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.mistral
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../test/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.test
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../function/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.function
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../fallback/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.fallback
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../wrapper/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.wrapper
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../providers/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.providers
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_graph/graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_graph/nodes/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.nodes
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_graph/persistence/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.persistence
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_graph/mermaid/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.mermaid
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_graph/exceptions/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.exceptions
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_evals/dataset/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.dataset
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_evals/evaluators/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.evaluators
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_evals/reporting/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.reporting
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_evals/otel/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.otel
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../pydantic_evals/generation/" class="md-nav__link">
        
  
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
  <a href="#pydantic_ai.models" class="md-nav__link">
    <span class="md-ellipsis">
      models
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.models.KnownModelName" class="md-nav__link">
    <span class="md-ellipsis">
      KnownModelName
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.models.ModelRequestParameters" class="md-nav__link">
    <span class="md-ellipsis">
      ModelRequestParameters
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.models.Model" class="md-nav__link">
    <span class="md-ellipsis">
      Model
    </span>
  </a>
  
    <nav class="md-nav" aria-label="Model">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.Model.request" class="md-nav__link">
    <span class="md-ellipsis">
      request
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.Model.request_stream" class="md-nav__link">
    <span class="md-ellipsis">
      request_stream
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.Model.model_name" class="md-nav__link">
    <span class="md-ellipsis">
      model_name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.Model.system" class="md-nav__link">
    <span class="md-ellipsis">
      system
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.Model.base_url" class="md-nav__link">
    <span class="md-ellipsis">
      base_url
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.models.StreamedResponse" class="md-nav__link">
    <span class="md-ellipsis">
      StreamedResponse
    </span>
  </a>
  
    <nav class="md-nav" aria-label="StreamedResponse">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.StreamedResponse.__aiter__" class="md-nav__link">
    <span class="md-ellipsis">
      __aiter__
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.StreamedResponse.get" class="md-nav__link">
    <span class="md-ellipsis">
      get
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.StreamedResponse.usage" class="md-nav__link">
    <span class="md-ellipsis">
      usage
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.StreamedResponse.model_name" class="md-nav__link">
    <span class="md-ellipsis">
      model_name
    </span>
  </a>
  
</li>
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.StreamedResponse.timestamp" class="md-nav__link">
    <span class="md-ellipsis">
      timestamp
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.models.ALLOW_MODEL_REQUESTS" class="md-nav__link">
    <span class="md-ellipsis">
      ALLOW_MODEL_REQUESTS
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.models.check_allow_model_requests" class="md-nav__link">
    <span class="md-ellipsis">
      check_allow_model_requests
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.models.override_allow_model_requests" class="md-nav__link">
    <span class="md-ellipsis">
      override_allow_model_requests
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
                
                  


  
  


<h1 id="pydantic_aimodels"><code>pydantic_ai.models</code></h1>


<div class="doc doc-object doc-module">



<a id="pydantic_ai.models"></a>
    <div class="doc doc-contents first">

        <p>Logic related to making requests to an LLM.</p>
<p>The aim here is to make a common interface for different LLMs, so that the rest of the code can be agnostic to the
specific LLM being used.</p>








  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h3 id="pydantic_ai.models.KnownModelName" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">KnownModelName</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span>

</h3>
<div class="language-python doc-signature highlight"><pre id="__code_0"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_0 > code"></button><code><span class="n">KnownModelName</span> <span class="o">=</span> <span class="n"><a class="autorefs autorefs-external" title="typing_extensions.TypeAliasType" href="https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.TypeAliasType">TypeAliasType</a></span><span class="p">(</span>
    <span class="s2">"KnownModelName"</span><span class="p">,</span>
    <span class="n"><a class="autorefs autorefs-external" title="typing_extensions.Literal" href="https://typing-extensions.readthedocs.io/en/latest/index.html#typing_extensions.Literal">Literal</a></span><span class="p">[</span>
        <span class="s2">"anthropic:claude-3-7-sonnet-latest"</span><span class="p">,</span>
        <span class="s2">"anthropic:claude-3-5-haiku-latest"</span><span class="p">,</span>
        <span class="s2">"anthropic:claude-3-5-sonnet-latest"</span><span class="p">,</span>
        <span class="s2">"anthropic:claude-3-opus-latest"</span><span class="p">,</span>
        <span class="s2">"claude-3-7-sonnet-latest"</span><span class="p">,</span>
        <span class="s2">"claude-3-5-haiku-latest"</span><span class="p">,</span>
        <span class="s2">"bedrock:amazon.titan-tg1-large"</span><span class="p">,</span>
        <span class="s2">"bedrock:amazon.titan-text-lite-v1"</span><span class="p">,</span>
        <span class="s2">"bedrock:amazon.titan-text-express-v1"</span><span class="p">,</span>
        <span class="s2">"bedrock:us.amazon.nova-pro-v1:0"</span><span class="p">,</span>
        <span class="s2">"bedrock:us.amazon.nova-lite-v1:0"</span><span class="p">,</span>
        <span class="s2">"bedrock:us.amazon.nova-micro-v1:0"</span><span class="p">,</span>
        <span class="s2">"bedrock:anthropic.claude-3-5-sonnet-20241022-v2:0"</span><span class="p">,</span>
        <span class="s2">"bedrock:us.anthropic.claude-3-5-sonnet-20241022-v2:0"</span><span class="p">,</span>
        <span class="s2">"bedrock:anthropic.claude-3-5-haiku-20241022-v1:0"</span><span class="p">,</span>
        <span class="s2">"bedrock:us.anthropic.claude-3-5-haiku-20241022-v1:0"</span><span class="p">,</span>
        <span class="s2">"bedrock:anthropic.claude-instant-v1"</span><span class="p">,</span>
        <span class="s2">"bedrock:anthropic.claude-v2:1"</span><span class="p">,</span>
        <span class="s2">"bedrock:anthropic.claude-v2"</span><span class="p">,</span>
        <span class="s2">"bedrock:anthropic.claude-3-sonnet-20240229-v1:0"</span><span class="p">,</span>
        <span class="s2">"bedrock:us.anthropic.claude-3-sonnet-20240229-v1:0"</span><span class="p">,</span>
        <span class="s2">"bedrock:anthropic.claude-3-haiku-20240307-v1:0"</span><span class="p">,</span>
        <span class="s2">"bedrock:us.anthropic.claude-3-haiku-20240307-v1:0"</span><span class="p">,</span>
        <span class="s2">"bedrock:anthropic.claude-3-opus-20240229-v1:0"</span><span class="p">,</span>
        <span class="s2">"bedrock:us.anthropic.claude-3-opus-20240229-v1:0"</span><span class="p">,</span>
        <span class="s2">"bedrock:anthropic.claude-3-5-sonnet-20240620-v1:0"</span><span class="p">,</span>
        <span class="s2">"bedrock:us.anthropic.claude-3-5-sonnet-20240620-v1:0"</span><span class="p">,</span>
        <span class="s2">"bedrock:anthropic.claude-3-7-sonnet-20250219-v1:0"</span><span class="p">,</span>
        <span class="s2">"bedrock:us.anthropic.claude-3-7-sonnet-20250219-v1:0"</span><span class="p">,</span>
        <span class="s2">"bedrock:cohere.command-text-v14"</span><span class="p">,</span>
        <span class="s2">"bedrock:cohere.command-r-v1:0"</span><span class="p">,</span>
        <span class="s2">"bedrock:cohere.command-r-plus-v1:0"</span><span class="p">,</span>
        <span class="s2">"bedrock:cohere.command-light-text-v14"</span><span class="p">,</span>
        <span class="s2">"bedrock:meta.llama3-8b-instruct-v1:0"</span><span class="p">,</span>
        <span class="s2">"bedrock:meta.llama3-70b-instruct-v1:0"</span><span class="p">,</span>
        <span class="s2">"bedrock:meta.llama3-1-8b-instruct-v1:0"</span><span class="p">,</span>
        <span class="s2">"bedrock:us.meta.llama3-1-8b-instruct-v1:0"</span><span class="p">,</span>
        <span class="s2">"bedrock:meta.llama3-1-70b-instruct-v1:0"</span><span class="p">,</span>
        <span class="s2">"bedrock:us.meta.llama3-1-70b-instruct-v1:0"</span><span class="p">,</span>
        <span class="s2">"bedrock:meta.llama3-1-405b-instruct-v1:0"</span><span class="p">,</span>
        <span class="s2">"bedrock:us.meta.llama3-2-11b-instruct-v1:0"</span><span class="p">,</span>
        <span class="s2">"bedrock:us.meta.llama3-2-90b-instruct-v1:0"</span><span class="p">,</span>
        <span class="s2">"bedrock:us.meta.llama3-2-1b-instruct-v1:0"</span><span class="p">,</span>
        <span class="s2">"bedrock:us.meta.llama3-2-3b-instruct-v1:0"</span><span class="p">,</span>
        <span class="s2">"bedrock:us.meta.llama3-3-70b-instruct-v1:0"</span><span class="p">,</span>
        <span class="s2">"bedrock:mistral.mistral-7b-instruct-v0:2"</span><span class="p">,</span>
        <span class="s2">"bedrock:mistral.mixtral-8x7b-instruct-v0:1"</span><span class="p">,</span>
        <span class="s2">"bedrock:mistral.mistral-large-2402-v1:0"</span><span class="p">,</span>
        <span class="s2">"bedrock:mistral.mistral-large-2407-v1:0"</span><span class="p">,</span>
        <span class="s2">"claude-3-5-sonnet-latest"</span><span class="p">,</span>
        <span class="s2">"claude-3-opus-latest"</span><span class="p">,</span>
        <span class="s2">"cohere:c4ai-aya-expanse-32b"</span><span class="p">,</span>
        <span class="s2">"cohere:c4ai-aya-expanse-8b"</span><span class="p">,</span>
        <span class="s2">"cohere:command"</span><span class="p">,</span>
        <span class="s2">"cohere:command-light"</span><span class="p">,</span>
        <span class="s2">"cohere:command-light-nightly"</span><span class="p">,</span>
        <span class="s2">"cohere:command-nightly"</span><span class="p">,</span>
        <span class="s2">"cohere:command-r"</span><span class="p">,</span>
        <span class="s2">"cohere:command-r-03-2024"</span><span class="p">,</span>
        <span class="s2">"cohere:command-r-08-2024"</span><span class="p">,</span>
        <span class="s2">"cohere:command-r-plus"</span><span class="p">,</span>
        <span class="s2">"cohere:command-r-plus-04-2024"</span><span class="p">,</span>
        <span class="s2">"cohere:command-r-plus-08-2024"</span><span class="p">,</span>
        <span class="s2">"cohere:command-r7b-12-2024"</span><span class="p">,</span>
        <span class="s2">"deepseek:deepseek-chat"</span><span class="p">,</span>
        <span class="s2">"deepseek:deepseek-reasoner"</span><span class="p">,</span>
        <span class="s2">"google-gla:gemini-1.0-pro"</span><span class="p">,</span>
        <span class="s2">"google-gla:gemini-1.5-flash"</span><span class="p">,</span>
        <span class="s2">"google-gla:gemini-1.5-flash-8b"</span><span class="p">,</span>
        <span class="s2">"google-gla:gemini-1.5-pro"</span><span class="p">,</span>
        <span class="s2">"google-gla:gemini-2.0-flash-exp"</span><span class="p">,</span>
        <span class="s2">"google-gla:gemini-2.0-flash-thinking-exp-01-21"</span><span class="p">,</span>
        <span class="s2">"google-gla:gemini-exp-1206"</span><span class="p">,</span>
        <span class="s2">"google-gla:gemini-2.0-flash"</span><span class="p">,</span>
        <span class="s2">"google-gla:gemini-2.0-flash-lite-preview-02-05"</span><span class="p">,</span>
        <span class="s2">"google-gla:gemini-2.0-pro-exp-02-05"</span><span class="p">,</span>
        <span class="s2">"google-gla:gemini-2.5-pro-exp-03-25"</span><span class="p">,</span>
        <span class="s2">"google-vertex:gemini-1.0-pro"</span><span class="p">,</span>
        <span class="s2">"google-vertex:gemini-1.5-flash"</span><span class="p">,</span>
        <span class="s2">"google-vertex:gemini-1.5-flash-8b"</span><span class="p">,</span>
        <span class="s2">"google-vertex:gemini-1.5-pro"</span><span class="p">,</span>
        <span class="s2">"google-vertex:gemini-2.0-flash-exp"</span><span class="p">,</span>
        <span class="s2">"google-vertex:gemini-2.0-flash-thinking-exp-01-21"</span><span class="p">,</span>
        <span class="s2">"google-vertex:gemini-exp-1206"</span><span class="p">,</span>
        <span class="s2">"google-vertex:gemini-2.0-flash"</span><span class="p">,</span>
        <span class="s2">"google-vertex:gemini-2.0-flash-lite-preview-02-05"</span><span class="p">,</span>
        <span class="s2">"google-vertex:gemini-2.0-pro-exp-02-05"</span><span class="p">,</span>
        <span class="s2">"google-vertex:gemini-2.5-pro-exp-03-25"</span><span class="p">,</span>
        <span class="s2">"gpt-3.5-turbo"</span><span class="p">,</span>
        <span class="s2">"gpt-3.5-turbo-0125"</span><span class="p">,</span>
        <span class="s2">"gpt-3.5-turbo-0301"</span><span class="p">,</span>
        <span class="s2">"gpt-3.5-turbo-0613"</span><span class="p">,</span>
        <span class="s2">"gpt-3.5-turbo-1106"</span><span class="p">,</span>
        <span class="s2">"gpt-3.5-turbo-16k"</span><span class="p">,</span>
        <span class="s2">"gpt-3.5-turbo-16k-0613"</span><span class="p">,</span>
        <span class="s2">"gpt-4"</span><span class="p">,</span>
        <span class="s2">"gpt-4-0125-preview"</span><span class="p">,</span>
        <span class="s2">"gpt-4-0314"</span><span class="p">,</span>
        <span class="s2">"gpt-4-0613"</span><span class="p">,</span>
        <span class="s2">"gpt-4-1106-preview"</span><span class="p">,</span>
        <span class="s2">"gpt-4-32k"</span><span class="p">,</span>
        <span class="s2">"gpt-4-32k-0314"</span><span class="p">,</span>
        <span class="s2">"gpt-4-32k-0613"</span><span class="p">,</span>
        <span class="s2">"gpt-4-turbo"</span><span class="p">,</span>
        <span class="s2">"gpt-4-turbo-2024-04-09"</span><span class="p">,</span>
        <span class="s2">"gpt-4-turbo-preview"</span><span class="p">,</span>
        <span class="s2">"gpt-4-vision-preview"</span><span class="p">,</span>
        <span class="s2">"gpt-4o"</span><span class="p">,</span>
        <span class="s2">"gpt-4o-2024-05-13"</span><span class="p">,</span>
        <span class="s2">"gpt-4o-2024-08-06"</span><span class="p">,</span>
        <span class="s2">"gpt-4o-2024-11-20"</span><span class="p">,</span>
        <span class="s2">"gpt-4o-audio-preview"</span><span class="p">,</span>
        <span class="s2">"gpt-4o-audio-preview-2024-10-01"</span><span class="p">,</span>
        <span class="s2">"gpt-4o-audio-preview-2024-12-17"</span><span class="p">,</span>
        <span class="s2">"gpt-4o-mini"</span><span class="p">,</span>
        <span class="s2">"gpt-4o-mini-2024-07-18"</span><span class="p">,</span>
        <span class="s2">"gpt-4o-mini-audio-preview"</span><span class="p">,</span>
        <span class="s2">"gpt-4o-mini-audio-preview-2024-12-17"</span><span class="p">,</span>
        <span class="s2">"gpt-4o-mini-search-preview"</span><span class="p">,</span>
        <span class="s2">"gpt-4o-mini-search-preview-2025-03-11"</span><span class="p">,</span>
        <span class="s2">"gpt-4o-search-preview"</span><span class="p">,</span>
        <span class="s2">"gpt-4o-search-preview-2025-03-11"</span><span class="p">,</span>
        <span class="s2">"groq:distil-whisper-large-v3-en"</span><span class="p">,</span>
        <span class="s2">"groq:gemma2-9b-it"</span><span class="p">,</span>
        <span class="s2">"groq:llama-3.3-70b-versatile"</span><span class="p">,</span>
        <span class="s2">"groq:llama-3.1-8b-instant"</span><span class="p">,</span>
        <span class="s2">"groq:llama-guard-3-8b"</span><span class="p">,</span>
        <span class="s2">"groq:llama3-70b-8192"</span><span class="p">,</span>
        <span class="s2">"groq:llama3-8b-8192"</span><span class="p">,</span>
        <span class="s2">"groq:whisper-large-v3"</span><span class="p">,</span>
        <span class="s2">"groq:whisper-large-v3-turbo"</span><span class="p">,</span>
        <span class="s2">"groq:playai-tts"</span><span class="p">,</span>
        <span class="s2">"groq:playai-tts-arabic"</span><span class="p">,</span>
        <span class="s2">"groq:qwen-qwq-32b"</span><span class="p">,</span>
        <span class="s2">"groq:mistral-saba-24b"</span><span class="p">,</span>
        <span class="s2">"groq:qwen-2.5-coder-32b"</span><span class="p">,</span>
        <span class="s2">"groq:qwen-2.5-32b"</span><span class="p">,</span>
        <span class="s2">"groq:deepseek-r1-distill-qwen-32b"</span><span class="p">,</span>
        <span class="s2">"groq:deepseek-r1-distill-llama-70b"</span><span class="p">,</span>
        <span class="s2">"groq:llama-3.3-70b-specdec"</span><span class="p">,</span>
        <span class="s2">"groq:llama-3.2-1b-preview"</span><span class="p">,</span>
        <span class="s2">"groq:llama-3.2-3b-preview"</span><span class="p">,</span>
        <span class="s2">"groq:llama-3.2-11b-vision-preview"</span><span class="p">,</span>
        <span class="s2">"groq:llama-3.2-90b-vision-preview"</span><span class="p">,</span>
        <span class="s2">"mistral:codestral-latest"</span><span class="p">,</span>
        <span class="s2">"mistral:mistral-large-latest"</span><span class="p">,</span>
        <span class="s2">"mistral:mistral-moderation-latest"</span><span class="p">,</span>
        <span class="s2">"mistral:mistral-small-latest"</span><span class="p">,</span>
        <span class="s2">"o1"</span><span class="p">,</span>
        <span class="s2">"o1-2024-12-17"</span><span class="p">,</span>
        <span class="s2">"o1-mini"</span><span class="p">,</span>
        <span class="s2">"o1-mini-2024-09-12"</span><span class="p">,</span>
        <span class="s2">"o1-preview"</span><span class="p">,</span>
        <span class="s2">"o1-preview-2024-09-12"</span><span class="p">,</span>
        <span class="s2">"o3-mini"</span><span class="p">,</span>
        <span class="s2">"o3-mini-2025-01-31"</span><span class="p">,</span>
        <span class="s2">"openai:chatgpt-4o-latest"</span><span class="p">,</span>
        <span class="s2">"openai:gpt-3.5-turbo"</span><span class="p">,</span>
        <span class="s2">"openai:gpt-3.5-turbo-0125"</span><span class="p">,</span>
        <span class="s2">"openai:gpt-3.5-turbo-0301"</span><span class="p">,</span>
        <span class="s2">"openai:gpt-3.5-turbo-0613"</span><span class="p">,</span>
        <span class="s2">"openai:gpt-3.5-turbo-1106"</span><span class="p">,</span>
        <span class="s2">"openai:gpt-3.5-turbo-16k"</span><span class="p">,</span>
        <span class="s2">"openai:gpt-3.5-turbo-16k-0613"</span><span class="p">,</span>
        <span class="s2">"openai:gpt-4"</span><span class="p">,</span>
        <span class="s2">"openai:gpt-4-0125-preview"</span><span class="p">,</span>
        <span class="s2">"openai:gpt-4-0314"</span><span class="p">,</span>
        <span class="s2">"openai:gpt-4-0613"</span><span class="p">,</span>
        <span class="s2">"openai:gpt-4-1106-preview"</span><span class="p">,</span>
        <span class="s2">"openai:gpt-4-32k"</span><span class="p">,</span>
        <span class="s2">"openai:gpt-4-32k-0314"</span><span class="p">,</span>
        <span class="s2">"openai:gpt-4-32k-0613"</span><span class="p">,</span>
        <span class="s2">"openai:gpt-4-turbo"</span><span class="p">,</span>
        <span class="s2">"openai:gpt-4-turbo-2024-04-09"</span><span class="p">,</span>
        <span class="s2">"openai:gpt-4-turbo-preview"</span><span class="p">,</span>
        <span class="s2">"openai:gpt-4-vision-preview"</span><span class="p">,</span>
        <span class="s2">"openai:gpt-4o"</span><span class="p">,</span>
        <span class="s2">"openai:gpt-4o-2024-05-13"</span><span class="p">,</span>
        <span class="s2">"openai:gpt-4o-2024-08-06"</span><span class="p">,</span>
        <span class="s2">"openai:gpt-4o-2024-11-20"</span><span class="p">,</span>
        <span class="s2">"openai:gpt-4o-audio-preview"</span><span class="p">,</span>
        <span class="s2">"openai:gpt-4o-audio-preview-2024-10-01"</span><span class="p">,</span>
        <span class="s2">"openai:gpt-4o-audio-preview-2024-12-17"</span><span class="p">,</span>
        <span class="s2">"openai:gpt-4o-mini"</span><span class="p">,</span>
        <span class="s2">"openai:gpt-4o-mini-2024-07-18"</span><span class="p">,</span>
        <span class="s2">"openai:gpt-4o-mini-audio-preview"</span><span class="p">,</span>
        <span class="s2">"openai:gpt-4o-mini-audio-preview-2024-12-17"</span><span class="p">,</span>
        <span class="s2">"openai:gpt-4o-mini-search-preview"</span><span class="p">,</span>
        <span class="s2">"openai:gpt-4o-mini-search-preview-2025-03-11"</span><span class="p">,</span>
        <span class="s2">"openai:gpt-4o-search-preview"</span><span class="p">,</span>
        <span class="s2">"openai:gpt-4o-search-preview-2025-03-11"</span><span class="p">,</span>
        <span class="s2">"openai:o1"</span><span class="p">,</span>
        <span class="s2">"openai:o1-2024-12-17"</span><span class="p">,</span>
        <span class="s2">"openai:o1-mini"</span><span class="p">,</span>
        <span class="s2">"openai:o1-mini-2024-09-12"</span><span class="p">,</span>
        <span class="s2">"openai:o1-preview"</span><span class="p">,</span>
        <span class="s2">"openai:o1-preview-2024-09-12"</span><span class="p">,</span>
        <span class="s2">"openai:o3-mini"</span><span class="p">,</span>
        <span class="s2">"openai:o3-mini-2025-01-31"</span><span class="p">,</span>
        <span class="s2">"test"</span><span class="p">,</span>
    <span class="p">],</span>
<span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Known model names that can be used with the <code>model</code> parameter of <a class="autorefs autorefs-internal" href="../../agent/#pydantic_ai.agent.Agent"><code>Agent</code></a>.</p>
<p><code>KnownModelName</code> is provided as a concise way to specify a model.</p>
    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.models.ModelRequestParameters" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">ModelRequestParameters</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">


        <p>Configuration for an agent's request to a model, specifically related to tools and result handling.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/models/__init__.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">241</span>
<span class="normal">242</span>
<span class="normal">243</span>
<span class="normal">244</span>
<span class="normal">245</span>
<span class="normal">246</span>
<span class="normal">247</span></pre></div></td><td class="code"><div><pre id="__code_1"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_1 > code"></button><code><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">ModelRequestParameters</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Configuration for an agent's request to a model, specifically related to tools and result handling."""</span>

    <span class="n">function_tools</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ToolDefinition</span><span class="p">]</span>
    <span class="n">allow_text_result</span><span class="p">:</span> <span class="nb">bool</span>
    <span class="n">result_tools</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ToolDefinition</span><span class="p">]</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">





  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.models.Model" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">Model</span>


</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-external" title="abc.ABC" href="https://docs.python.org/3/library/abc.html#abc.ABC">ABC</a></code></p>


        <p>Abstract class for a model.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/models/__init__.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">250</span>
<span class="normal">251</span>
<span class="normal">252</span>
<span class="normal">253</span>
<span class="normal">254</span>
<span class="normal">255</span>
<span class="normal">256</span>
<span class="normal">257</span>
<span class="normal">258</span>
<span class="normal">259</span>
<span class="normal">260</span>
<span class="normal">261</span>
<span class="normal">262</span>
<span class="normal">263</span>
<span class="normal">264</span>
<span class="normal">265</span>
<span class="normal">266</span>
<span class="normal">267</span>
<span class="normal">268</span>
<span class="normal">269</span>
<span class="normal">270</span>
<span class="normal">271</span>
<span class="normal">272</span>
<span class="normal">273</span>
<span class="normal">274</span>
<span class="normal">275</span>
<span class="normal">276</span>
<span class="normal">277</span>
<span class="normal">278</span>
<span class="normal">279</span>
<span class="normal">280</span>
<span class="normal">281</span>
<span class="normal">282</span>
<span class="normal">283</span>
<span class="normal">284</span>
<span class="normal">285</span>
<span class="normal">286</span>
<span class="normal">287</span>
<span class="normal">288</span>
<span class="normal">289</span>
<span class="normal">290</span>
<span class="normal">291</span>
<span class="normal">292</span>
<span class="normal">293</span>
<span class="normal">294</span>
<span class="normal">295</span>
<span class="normal">296</span>
<span class="normal">297</span>
<span class="normal">298</span></pre></div></td><td class="code"><div><pre id="__code_2"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_2 > code"></button><code><span class="k">class</span><span class="w"> </span><span class="nc">Model</span><span class="p">(</span><span class="n">ABC</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Abstract class for a model."""</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">request</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">messages</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ModelMessage</span><span class="p">],</span>
        <span class="n">model_settings</span><span class="p">:</span> <span class="n">ModelSettings</span> <span class="o">|</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">model_request_parameters</span><span class="p">:</span> <span class="n">ModelRequestParameters</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">tuple</span><span class="p">[</span><span class="n">ModelResponse</span><span class="p">,</span> <span class="n">Usage</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Make a request to the model."""</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>

    <span class="nd">@asynccontextmanager</span>
    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">request_stream</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">messages</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ModelMessage</span><span class="p">],</span>
        <span class="n">model_settings</span><span class="p">:</span> <span class="n">ModelSettings</span> <span class="o">|</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">model_request_parameters</span><span class="p">:</span> <span class="n">ModelRequestParameters</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="n">StreamedResponse</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Make a request to the model and return a streaming response."""</span>
        <span class="c1"># This method is not required, but you need to implement it if you want to support streamed responses</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="sa">f</span><span class="s1">'Streamed requests not supported by this </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="vm">__class__</span><span class="o">.</span><span class="vm">__name__</span><span class="si">}</span><span class="s1">'</span><span class="p">)</span>
        <span class="c1"># yield is required to make this a generator for type checking</span>
        <span class="c1"># noinspection PyUnreachableCode</span>
        <span class="k">yield</span>  <span class="c1"># pragma: no cover</span>

    <span class="nd">@property</span>
    <span class="nd">@abstractmethod</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">model_name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""The model name."""</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>

    <span class="nd">@property</span>
    <span class="nd">@abstractmethod</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">system</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""The system / model provider, ex: openai.</span>

<span class="sd">        Use to populate the `gen_ai.system` OpenTelemetry semantic convention attribute,</span>
<span class="sd">        so should use well-known values listed in</span>
<span class="sd">        https://opentelemetry.io/docs/specs/semconv/attributes-registry/gen-ai/#gen-ai-system</span>
<span class="sd">        when applicable.</span>
<span class="sd">        """</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">base_url</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""The base URL for the provider API, if available."""</span>
        <span class="k">return</span> <span class="kc">None</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.models.Model.request" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">request</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-abstractmethod"><code>abstractmethod</code></small>
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_3"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_3 > code"></button><code><span class="nf">request</span><span class="p">(</span>
    <span class="n">messages</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelMessage" href="../../messages/#pydantic_ai.messages.ModelMessage">ModelMessage</a></span><span class="p">],</span>
    <span class="n">model_settings</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.settings.ModelSettings" href="../../settings/#pydantic_ai.settings.ModelSettings">ModelSettings</a></span> <span class="o">|</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model_request_parameters</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.ModelRequestParameters" href="#pydantic_ai.models.ModelRequestParameters">ModelRequestParameters</a></span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#tuple">tuple</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelResponse" href="../../messages/#pydantic_ai.messages.ModelResponse">ModelResponse</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.usage.Usage" href="../../usage/#pydantic_ai.usage.Usage">Usage</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Make a request to the model.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/models/__init__.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">253</span>
<span class="normal">254</span>
<span class="normal">255</span>
<span class="normal">256</span>
<span class="normal">257</span>
<span class="normal">258</span>
<span class="normal">259</span>
<span class="normal">260</span>
<span class="normal">261</span></pre></div></td><td class="code"><div><pre id="__code_4"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_4 > code"></button><code><span class="nd">@abstractmethod</span>
<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">request</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">messages</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ModelMessage</span><span class="p">],</span>
    <span class="n">model_settings</span><span class="p">:</span> <span class="n">ModelSettings</span> <span class="o">|</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model_request_parameters</span><span class="p">:</span> <span class="n">ModelRequestParameters</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">tuple</span><span class="p">[</span><span class="n">ModelResponse</span><span class="p">,</span> <span class="n">Usage</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Make a request to the model."""</span>
    <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.models.Model.request_stream" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">request_stream</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-async"><code>async</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_5"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_5 > code"></button><code><span class="nf">request_stream</span><span class="p">(</span>
    <span class="n">messages</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#list">list</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelMessage" href="../../messages/#pydantic_ai.messages.ModelMessage">ModelMessage</a></span><span class="p">],</span>
    <span class="n">model_settings</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.settings.ModelSettings" href="../../settings/#pydantic_ai.settings.ModelSettings">ModelSettings</a></span> <span class="o">|</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model_request_parameters</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.ModelRequestParameters" href="#pydantic_ai.models.ModelRequestParameters">ModelRequestParameters</a></span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.AsyncIterator" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator">AsyncIterator</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.StreamedResponse" href="#pydantic_ai.models.StreamedResponse">StreamedResponse</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Make a request to the model and return a streaming response.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/models/__init__.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">263</span>
<span class="normal">264</span>
<span class="normal">265</span>
<span class="normal">266</span>
<span class="normal">267</span>
<span class="normal">268</span>
<span class="normal">269</span>
<span class="normal">270</span>
<span class="normal">271</span>
<span class="normal">272</span>
<span class="normal">273</span>
<span class="normal">274</span>
<span class="normal">275</span></pre></div></td><td class="code"><div><pre id="__code_6"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_6 > code"></button><code><span class="nd">@asynccontextmanager</span>
<span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">request_stream</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">messages</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ModelMessage</span><span class="p">],</span>
    <span class="n">model_settings</span><span class="p">:</span> <span class="n">ModelSettings</span> <span class="o">|</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">model_request_parameters</span><span class="p">:</span> <span class="n">ModelRequestParameters</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="n">StreamedResponse</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Make a request to the model and return a streaming response."""</span>
    <span class="c1"># This method is not required, but you need to implement it if you want to support streamed responses</span>
    <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">(</span><span class="sa">f</span><span class="s1">'Streamed requests not supported by this </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="vm">__class__</span><span class="o">.</span><span class="vm">__name__</span><span class="si">}</span><span class="s1">'</span><span class="p">)</span>
    <span class="c1"># yield is required to make this a generator for type checking</span>
    <span class="c1"># noinspection PyUnreachableCode</span>
    <span class="k">yield</span>  <span class="c1"># pragma: no cover</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.models.Model.model_name" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">model_name</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-abstractmethod"><code>abstractmethod</code></small>
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_7"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_7 > code"></button><code><span class="n">model_name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The model name.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.models.Model.system" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">system</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-abstractmethod"><code>abstractmethod</code></small>
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_8"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_8 > code"></button><code><span class="n">system</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The system / model provider, ex: openai.</p>
<p>Use to populate the <code>gen_ai.system</code> OpenTelemetry semantic convention attribute,
so should use well-known values listed in
https://opentelemetry.io/docs/specs/semconv/attributes-registry/gen-ai/#gen-ai-system
when applicable.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.models.Model.base_url" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">base_url</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_9"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_9 > code"></button><code><span class="n">base_url</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The base URL for the provider API, if available.</p>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.models.StreamedResponse" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">StreamedResponse</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-external" title="abc.ABC" href="https://docs.python.org/3/library/abc.html#abc.ABC">ABC</a></code></p>


        <p>Streamed response from an LLM when calling a tool.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/models/__init__.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">301</span>
<span class="normal">302</span>
<span class="normal">303</span>
<span class="normal">304</span>
<span class="normal">305</span>
<span class="normal">306</span>
<span class="normal">307</span>
<span class="normal">308</span>
<span class="normal">309</span>
<span class="normal">310</span>
<span class="normal">311</span>
<span class="normal">312</span>
<span class="normal">313</span>
<span class="normal">314</span>
<span class="normal">315</span>
<span class="normal">316</span>
<span class="normal">317</span>
<span class="normal">318</span>
<span class="normal">319</span>
<span class="normal">320</span>
<span class="normal">321</span>
<span class="normal">322</span>
<span class="normal">323</span>
<span class="normal">324</span>
<span class="normal">325</span>
<span class="normal">326</span>
<span class="normal">327</span>
<span class="normal">328</span>
<span class="normal">329</span>
<span class="normal">330</span>
<span class="normal">331</span>
<span class="normal">332</span>
<span class="normal">333</span>
<span class="normal">334</span>
<span class="normal">335</span>
<span class="normal">336</span>
<span class="normal">337</span>
<span class="normal">338</span>
<span class="normal">339</span>
<span class="normal">340</span>
<span class="normal">341</span>
<span class="normal">342</span>
<span class="normal">343</span>
<span class="normal">344</span>
<span class="normal">345</span>
<span class="normal">346</span>
<span class="normal">347</span>
<span class="normal">348</span></pre></div></td><td class="code"><div><pre id="__code_10"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_10 > code"></button><code tabindex="0"><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">StreamedResponse</span><span class="p">(</span><span class="n">ABC</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Streamed response from an LLM when calling a tool."""</span>

    <span class="n">_parts_manager</span><span class="p">:</span> <span class="n">ModelResponsePartsManager</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="n">ModelResponsePartsManager</span><span class="p">,</span> <span class="n">init</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
    <span class="n">_event_iterator</span><span class="p">:</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="n">ModelResponseStreamEvent</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">default</span><span class="o">=</span><span class="kc">None</span><span class="p">,</span> <span class="n">init</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
    <span class="n">_usage</span><span class="p">:</span> <span class="n">Usage</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="n">default_factory</span><span class="o">=</span><span class="n">Usage</span><span class="p">,</span> <span class="n">init</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="fm">__aiter__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="n">ModelResponseStreamEvent</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Stream the response as an async iterable of [`ModelResponseStreamEvent`][pydantic_ai.messages.ModelResponseStreamEvent]s."""</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_event_iterator</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_event_iterator</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_event_iterator</span><span class="p">()</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_event_iterator</span>

    <span class="nd">@abstractmethod</span>
    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">_get_event_iterator</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="n">ModelResponseStreamEvent</span><span class="p">]:</span>
<span class="w">        </span><span class="sd">"""Return an async iterator of [`ModelResponseStreamEvent`][pydantic_ai.messages.ModelResponseStreamEvent]s.</span>

<span class="sd">        This method should be implemented by subclasses to translate the vendor-specific stream of events into</span>
<span class="sd">        pydantic_ai-format events.</span>

<span class="sd">        It should use the `_parts_manager` to handle deltas, and should update the `_usage` attributes as it goes.</span>
<span class="sd">        """</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
        <span class="c1"># noinspection PyUnreachableCode</span>
        <span class="k">yield</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ModelResponse</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Build a [`ModelResponse`][pydantic_ai.messages.ModelResponse] from the data received from the stream so far."""</span>
        <span class="k">return</span> <span class="n">ModelResponse</span><span class="p">(</span>
            <span class="n">parts</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_parts_manager</span><span class="o">.</span><span class="n">get_parts</span><span class="p">(),</span> <span class="n">model_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">model_name</span><span class="p">,</span> <span class="n">timestamp</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">timestamp</span>
        <span class="p">)</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">usage</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Usage</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get the usage of the response so far. This will not be the final usage until the stream is exhausted."""</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_usage</span>

    <span class="nd">@property</span>
    <span class="nd">@abstractmethod</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">model_name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get the model name of the response."""</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>

    <span class="nd">@property</span>
    <span class="nd">@abstractmethod</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">timestamp</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">datetime</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Get the timestamp of the response."""</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.models.StreamedResponse.__aiter__" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">__aiter__</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_11"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_11 > code"></button><code><span class="fm">__aiter__</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="nf"><a class="autorefs autorefs-external" title="collections.abc.AsyncIterator" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.AsyncIterator">AsyncIterator</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelResponseStreamEvent" href="../../messages/#pydantic_ai.messages.ModelResponseStreamEvent">ModelResponseStreamEvent</a></span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Stream the response as an async iterable of <a class="autorefs autorefs-internal" href="../../messages/#pydantic_ai.messages.ModelResponseStreamEvent"><code>ModelResponseStreamEvent</code></a>s.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/models/__init__.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">309</span>
<span class="normal">310</span>
<span class="normal">311</span>
<span class="normal">312</span>
<span class="normal">313</span></pre></div></td><td class="code"><div><pre id="__code_12"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_12 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="fm">__aiter__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="n">ModelResponseStreamEvent</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Stream the response as an async iterable of [`ModelResponseStreamEvent`][pydantic_ai.messages.ModelResponseStreamEvent]s."""</span>
    <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">_event_iterator</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_event_iterator</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">_get_event_iterator</span><span class="p">()</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_event_iterator</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>










<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.models.StreamedResponse.get" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">get</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_13"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_13 > code"></button><code><span class="nf">get</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.messages.ModelResponse" href="../../messages/#pydantic_ai.messages.ModelResponse">ModelResponse</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Build a <a class="autorefs autorefs-internal" href="../../messages/#pydantic_ai.messages.ModelResponse"><code>ModelResponse</code></a> from the data received from the stream so far.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/models/__init__.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">328</span>
<span class="normal">329</span>
<span class="normal">330</span>
<span class="normal">331</span>
<span class="normal">332</span></pre></div></td><td class="code"><div><pre id="__code_14"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_14 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="nf">get</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">ModelResponse</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Build a [`ModelResponse`][pydantic_ai.messages.ModelResponse] from the data received from the stream so far."""</span>
    <span class="k">return</span> <span class="n">ModelResponse</span><span class="p">(</span>
        <span class="n">parts</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">_parts_manager</span><span class="o">.</span><span class="n">get_parts</span><span class="p">(),</span> <span class="n">model_name</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">model_name</span><span class="p">,</span> <span class="n">timestamp</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">timestamp</span>
    <span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.models.StreamedResponse.usage" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">usage</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_15"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_15 > code"></button><code><span class="nf">usage</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.usage.Usage" href="../../usage/#pydantic_ai.usage.Usage">Usage</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Get the usage of the response so far. This will not be the final usage until the stream is exhausted.</p>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/models/__init__.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">334</span>
<span class="normal">335</span>
<span class="normal">336</span></pre></div></td><td class="code"><div><pre id="__code_16"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_16 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="nf">usage</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Usage</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Get the usage of the response so far. This will not be the final usage until the stream is exhausted."""</span>
    <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_usage</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.models.StreamedResponse.model_name" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">model_name</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-abstractmethod"><code>abstractmethod</code></small>
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_17"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_17 > code"></button><code><span class="n">model_name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Get the model name of the response.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.models.StreamedResponse.timestamp" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">timestamp</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-abstractmethod"><code>abstractmethod</code></small>
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_18"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_18 > code"></button><code><span class="n">timestamp</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="datetime.datetime" href="https://docs.python.org/3/library/datetime.html#datetime.datetime">datetime</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Get the timestamp of the response.</p>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-attribute">



<h3 id="pydantic_ai.models.ALLOW_MODEL_REQUESTS" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">ALLOW_MODEL_REQUESTS</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-module-attribute"><code>module-attribute</code></small>
  </span>

</h3>
<div class="language-python doc-signature highlight"><pre id="__code_19"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_19 > code"></button><code><span class="n">ALLOW_MODEL_REQUESTS</span> <span class="o">=</span> <span class="kc">True</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Whether to allow requests to models.</p>
<p>This global setting allows you to disable request to most models, e.g. to make sure you don't accidentally
make costly requests to a model during tests.</p>
<p>The testing models <a class="autorefs autorefs-internal" href="../test/#pydantic_ai.models.test.TestModel"><code>TestModel</code></a> and
<a class="autorefs autorefs-internal" href="../function/#pydantic_ai.models.function.FunctionModel"><code>FunctionModel</code></a> are no affected by this setting.</p>
    </div>

</div>






<div class="doc doc-object doc-function">


<h3 id="pydantic_ai.models.check_allow_model_requests" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">check_allow_model_requests</span>


</h3>
<div class="language-python doc-signature highlight"><pre id="__code_20"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_20 > code"></button><code><span class="nf">check_allow_model_requests</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Check if model requests are allowed.</p>
<p>If you're defining your own models that have costs or latency associated with their use, you should call this in
<a class="autorefs autorefs-internal" href="#pydantic_ai.models.Model.request"><code>Model.request</code></a> and <a class="autorefs autorefs-internal" href="#pydantic_ai.models.Model.request_stream"><code>Model.request_stream</code></a>.</p>


<p><span class="doc-section-title">Raises:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Type</th>
          <th>Description</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/exceptions.html#RuntimeError">RuntimeError</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>If model requests are not allowed.</p>
              </div>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/models/__init__.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">362</span>
<span class="normal">363</span>
<span class="normal">364</span>
<span class="normal">365</span>
<span class="normal">366</span>
<span class="normal">367</span>
<span class="normal">368</span>
<span class="normal">369</span>
<span class="normal">370</span>
<span class="normal">371</span>
<span class="normal">372</span></pre></div></td><td class="code"><div><pre id="__code_21"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_21 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="nf">check_allow_model_requests</span><span class="p">()</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Check if model requests are allowed.</span>

<span class="sd">    If you're defining your own models that have costs or latency associated with their use, you should call this in</span>
<span class="sd">    [`Model.request`][pydantic_ai.models.Model.request] and [`Model.request_stream`][pydantic_ai.models.Model.request_stream].</span>

<span class="sd">    Raises:</span>
<span class="sd">        RuntimeError: If model requests are not allowed.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="ow">not</span> <span class="n">ALLOW_MODEL_REQUESTS</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">RuntimeError</span><span class="p">(</span><span class="s1">'Model requests are not allowed, since ALLOW_MODEL_REQUESTS is False'</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>






<div class="doc doc-object doc-function">


<h3 id="pydantic_ai.models.override_allow_model_requests" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">override_allow_model_requests</span>


</h3>
<div class="language-python doc-signature highlight"><pre id="__code_22"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_22 > code"></button><code><span class="nf">override_allow_model_requests</span><span class="p">(</span>
    <span class="n">allow_model_requests</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Iterator" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Iterator">Iterator</a></span><span class="p">[</span><span class="kc">None</span><span class="p">]</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Context manager to temporarily override <a class="autorefs autorefs-internal" href="#pydantic_ai.models.ALLOW_MODEL_REQUESTS"><code>ALLOW_MODEL_REQUESTS</code></a>.</p>


<p><span class="doc-section-title">Parameters:</span></p>
    <div class="md-typeset__scrollwrap"><div class="md-typeset__table"><table>
      <thead>
        <tr>
          <th>Name</th>
          <th>Type</th>
          <th>Description</th>
          <th>Default</th>
        </tr>
      </thead>
      <tbody>
          <tr class="doc-section-item">
            <td>
                <code>allow_model_requests</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#bool">bool</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Whether to allow model requests within the context.</p>
              </div>
            </td>
            <td>
                <em>required</em>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/models/__init__.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">375</span>
<span class="normal">376</span>
<span class="normal">377</span>
<span class="normal">378</span>
<span class="normal">379</span>
<span class="normal">380</span>
<span class="normal">381</span>
<span class="normal">382</span>
<span class="normal">383</span>
<span class="normal">384</span>
<span class="normal">385</span>
<span class="normal">386</span>
<span class="normal">387</span>
<span class="normal">388</span></pre></div></td><td class="code"><div><pre id="__code_23"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_23 > code"></button><code tabindex="0"><span class="nd">@contextmanager</span>
<span class="k">def</span><span class="w"> </span><span class="nf">override_allow_model_requests</span><span class="p">(</span><span class="n">allow_model_requests</span><span class="p">:</span> <span class="nb">bool</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Iterator</span><span class="p">[</span><span class="kc">None</span><span class="p">]:</span>
<span class="w">    </span><span class="sd">"""Context manager to temporarily override [`ALLOW_MODEL_REQUESTS`][pydantic_ai.models.ALLOW_MODEL_REQUESTS].</span>

<span class="sd">    Args:</span>
<span class="sd">        allow_model_requests: Whether to allow model requests within the context.</span>
<span class="sd">    """</span>
    <span class="k">global</span> <span class="n">ALLOW_MODEL_REQUESTS</span>
    <span class="n">old_value</span> <span class="o">=</span> <span class="n">ALLOW_MODEL_REQUESTS</span>
    <span class="n">ALLOW_MODEL_REQUESTS</span> <span class="o">=</span> <span class="n">allow_model_requests</span>  <span class="c1"># pyright: ignore[reportConstantRedefinition]</span>
    <span class="k">try</span><span class="p">:</span>
        <span class="k">yield</span>
    <span class="k">finally</span><span class="p">:</span>
        <span class="n">ALLOW_MODEL_REQUESTS</span> <span class="o">=</span> <span class="n">old_value</span>  <span class="c1"># pyright: ignore[reportConstantRedefinition]</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>




  </div>

    </div>

</div>







  
  






                
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
    
    
    <script id="__config" type="application/json">{"base": "../../..", "features": ["search.suggest", "search.highlight", "content.tabs.link", "content.code.annotate", "content.code.copy", "content.code.select", "navigation.path", "navigation.indexes", "navigation.sections", "navigation.tracking", "toc.follow"], "search": "../../../assets/javascripts/workers/search.f8cc74c7.min.js", "translations": {"clipboard.copied": "Copied to clipboard", "clipboard.copy": "Copy to clipboard", "search.result.more.one": "1 more on this page", "search.result.more.other": "# more on this page", "search.result.none": "No matching documents", "search.result.one": "1 matching document", "search.result.other": "# matching documents", "search.result.placeholder": "Type to start searching", "search.result.term.missing": "Missing", "select.version": "Select version"}}</script>
    
    
      <script src="../../../assets/javascripts/bundle.f1b6f286.min.js"></script>
      
        <script src="/flarelytics/client.js"></script>
      
        <script src="https://cdn.jsdelivr.net/npm/algoliasearch@5.20.0/dist/lite/builds/browser.umd.js"></script>
      
        <script src="https://cdn.jsdelivr.net/npm/instantsearch.js@4.77.3/dist/instantsearch.production.min.js"></script>
      
        <script src="/javascripts/algolia-search.js"></script>
      
    
  <script id="init-glightbox">const lightbox = GLightbox({"touchNavigation": true, "loop": false, "zoomable": true, "draggable": true, "openEffect": "zoom", "closeEffect": "zoom", "slideEffect": "slide"});
document$.subscribe(() => { lightbox.reload() });
</script>
</body></html>