<!DOCTYPE html><html lang="en" class="js-focus-visible js" data-js-focus-visible=""><head>
    
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width,initial-scale=1">
      
        <meta name="description" content="Agent Framework / shim to use Pydantic with LLMs">
      
      
      
        <link rel="canonical" href="https://ai.pydantic.dev/api/providers/">
      
      
        <link rel="prev" href="../models/wrapper/">
      
      
        <link rel="next" href="../pydantic_graph/graph/">
      
      
      <link rel="icon" href="../../favicon.ico">
      <meta name="generator" content="mkdocs-1.6.1, mkdocs-material-9.6.5">
    
    
      
        <title>pydantic_ai.providers - PydanticAI</title>
      
    
    
      <link rel="stylesheet" href="../../assets/stylesheets/main.8608ea7d.min.css">
      
        
        <link rel="stylesheet" href="../../assets/stylesheets/palette.06af60db.min.css">
      
      


    
    
      
    
    
      
        
        
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300i,400,400i,700,700i%7CRoboto+Mono:400,400i,700,700i&amp;display=fallback">
        <style>:root{--md-text-font:"Roboto";--md-code-font:"Roboto Mono"}</style>
      
    
    
      <link rel="stylesheet" href="../../assets/_mkdocstrings.css">
    
      <link rel="stylesheet" href="../../extra/tweaks.css">
    
    <script>__md_scope=new URL("../..",location),__md_hash=e=>[...e].reduce(((e,_)=>(e<<5)-e+_.charCodeAt(0)),0),__md_get=(e,_=localStorage,t=__md_scope)=>JSON.parse(_.getItem(t.pathname+"."+e)),__md_set=(e,_,t=localStorage,a=__md_scope)=>{try{t.setItem(a.pathname+"."+e,JSON.stringify(_))}catch(e){}}</script>
    
      

    
    
      
        <meta property="og:type" content="website">
      
        <meta property="og:title" content="pydantic_ai.providers - PydanticAI">
      
        <meta property="og:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta property="og:image" content="https://ai.pydantic.dev/assets/images/social/api/providers.png">
      
        <meta property="og:image:type" content="image/png">
      
        <meta property="og:image:width" content="1200">
      
        <meta property="og:image:height" content="630">
      
        <meta property="og:url" content="https://ai.pydantic.dev/api/providers/">
      
        <meta name="twitter:card" content="summary_large_image">
      
        <meta name="twitter:title" content="pydantic_ai.providers - PydanticAI">
      
        <meta name="twitter:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta name="twitter:image" content="https://ai.pydantic.dev/assets/images/social/api/providers.png">
      
    
    
   <link href="../../assets/stylesheets/glightbox.min.css" rel="stylesheet"><style>
    html.glightbox-open { overflow: initial; height: 100%; }
    .gslide-title { margin-top: 0px; user-select: text; }
    .gslide-desc { color: #666; user-select: text; }
    .gslide-image img { background: white; }
    .gscrollbar-fixer { padding-right: 15px; }
    .gdesc-inner { font-size: 0.75rem; }
    body[data-md-color-scheme="slate"] .gdesc-inner { background: var(--md-default-bg-color);}
    body[data-md-color-scheme="slate"] .gslide-title { color: var(--md-default-fg-color);}
    body[data-md-color-scheme="slate"] .gslide-desc { color: var(--md-default-fg-color);}</style> <script src="../../assets/javascripts/glightbox.min.js"></script><meta name="theme-color" content="#e92063"><meta name="color-scheme" content="light"></head>
  
  
    
    
      
    
    
    
    
    <body dir="ltr" data-md-color-scheme="default" data-md-color-primary="pink" data-md-color-accent="pink" data-md-color-media="(prefers-color-scheme)">
  
    
    <input class="md-toggle" data-md-toggle="drawer" type="checkbox" id="__drawer" autocomplete="off">
    <input class="md-toggle" data-md-toggle="search" type="checkbox" id="__search" autocomplete="off">
    <label class="md-overlay" for="__drawer"></label>
    <div data-md-component="skip">
      
        
        <a href="#pydantic_aiproviders" class="md-skip">
          Skip to content
        </a>
      
    </div>
    <div data-md-component="announce">
      
    </div>
    
    
      

  

<header class="md-header md-header--shadow" data-md-component="header">
  <nav class="md-header__inner md-grid" aria-label="Header">
    <a href="../.." title="PydanticAI" class="md-header__button md-logo" aria-label="PydanticAI" data-md-component="logo">
      
  <img src="../../img/logo-white.svg" alt="logo">

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
            
              pydantic_ai.providers
            
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
    <a href="../.." title="PydanticAI" class="md-nav__button md-logo" aria-label="PydanticAI" data-md-component="logo">
      
  <img src="../../img/logo-white.svg" alt="logo">

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
      <a href="../.." class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Introduction
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../install/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Installation
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../help/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Getting Help
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../contributing/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Contributing
    
  </span>
  

      </a>
    </li>
  

    
      
      
  
  
  
  
    <li class="md-nav__item">
      <a href="../../troubleshooting/" class="md-nav__link">
        
  
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
      <a href="../../agents/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Agents
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../models/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Models
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../dependencies/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Dependencies
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Function Tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../common-tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Common Tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../results/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Results
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../message-history/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Messages and chat history
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../testing/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Unit testing
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../logfire/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Debugging and Monitoring
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../multi-agent-applications/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Multi-agent Applications
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Graphs
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../evals/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Evals
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../input/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Image, Audio &amp; Document Input
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    
    
      
        
          
        
      
        
      
        
      
        
      
    
    
      
    
    
    <li class="md-nav__item md-nav__item--nested">
      
        
        
        <input class="md-nav__toggle md-toggle " type="checkbox" id="__nav_6_14">
        
          
          
          <div class="md-nav__link md-nav__container">
            <a href="../../mcp/" class="md-nav__link ">
              
  
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
      <a href="../../mcp/client/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Client
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../mcp/server/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Server
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../mcp/run-python/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    MCP Run Python
    
  </span>
  

      </a>
    </li>
  

              
            
          </ul>
        </nav>
      
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../cli/" class="md-nav__link">
        
  
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
            <a href="../../examples/" class="md-nav__link ">
              
  
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
      <a href="../../examples/pydantic-model/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Pydantic Model
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../examples/weather-agent/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Weather agent
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../examples/bank-support/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Bank support
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../examples/sql-gen/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    SQL Generation
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../examples/flight-booking/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Flight booking
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../examples/rag/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    RAG
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../examples/stream-markdown/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Stream markdown
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../examples/stream-whales/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Stream whales
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../examples/chat-app/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    Chat App with FastAPI
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../../examples/question-graph/" class="md-nav__link">
        
  
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
      <a href="../agent/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.agent
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../common_tools/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.common_tools
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../result/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.result
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../messages/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.messages
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../exceptions/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.exceptions
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../settings/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.settings
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../usage/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.usage
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../mcp/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.mcp
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../format_as_xml/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.format_as_xml
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/base/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/openai/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.openai
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/anthropic/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.anthropic
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/bedrock/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.bedrock
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/cohere/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.cohere
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/gemini/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.gemini
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/groq/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.groq
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/instrumented/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.instrumented
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/mistral/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.mistral
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/test/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.test
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/function/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.function
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/fallback/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.fallback
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../models/wrapper/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.wrapper
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
    
  
  
  
    <li class="md-nav__item md-nav__item--active">
      
      <input class="md-nav__toggle md-toggle" type="checkbox" id="__toc">
      
      
        
      
      
        <label class="md-nav__link md-nav__link--active" for="__toc">
          
  
  <span class="md-ellipsis">
    pydantic_ai.providers
    
  </span>
  

          <span class="md-nav__icon md-icon"></span>
        </label>
      
      <a href="./" class="md-nav__link md-nav__link--active">
        
  
  <span class="md-ellipsis">
    pydantic_ai.providers
    
  </span>
  

      </a>
      
        

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
    
  
  
    <label class="md-nav__title" for="__toc">
      <span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
    <ul class="md-nav__list" data-md-component="toc">
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.providers.Provider" class="md-nav__link">
    <span class="md-ellipsis">
      Provider
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.providers.Provider.name" class="md-nav__link">
    <span class="md-ellipsis">
      name
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.providers.Provider.base_url" class="md-nav__link">
    <span class="md-ellipsis">
      base_url
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.providers.Provider.client" class="md-nav__link">
    <span class="md-ellipsis">
      client
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.providers.google_vertex" class="md-nav__link">
    <span class="md-ellipsis">
      google_vertex
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.providers.google_vertex.GoogleVertexProvider" class="md-nav__link">
    <span class="md-ellipsis">
      GoogleVertexProvider
    </span>
  </a>
  
    <nav class="md-nav" aria-label="GoogleVertexProvider">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.providers.google_vertex.GoogleVertexProvider.__init__" class="md-nav__link">
    <span class="md-ellipsis">
      __init__
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.providers.openai" class="md-nav__link">
    <span class="md-ellipsis">
      openai
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.providers.openai.OpenAIProvider" class="md-nav__link">
    <span class="md-ellipsis">
      OpenAIProvider
    </span>
  </a>
  
    <nav class="md-nav" aria-label="OpenAIProvider">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.providers.openai.OpenAIProvider.__init__" class="md-nav__link">
    <span class="md-ellipsis">
      __init__
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.providers.deepseek" class="md-nav__link">
    <span class="md-ellipsis">
      deepseek
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.providers.deepseek.DeepSeekProvider" class="md-nav__link">
    <span class="md-ellipsis">
      DeepSeekProvider
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.providers.bedrock" class="md-nav__link">
    <span class="md-ellipsis">
      bedrock
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.providers.bedrock.BedrockProvider" class="md-nav__link">
    <span class="md-ellipsis">
      BedrockProvider
    </span>
  </a>
  
    <nav class="md-nav" aria-label="BedrockProvider">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.providers.bedrock.BedrockProvider.__init__" class="md-nav__link">
    <span class="md-ellipsis">
      __init__
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.providers.groq" class="md-nav__link">
    <span class="md-ellipsis">
      groq
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.providers.groq.GroqProvider" class="md-nav__link">
    <span class="md-ellipsis">
      GroqProvider
    </span>
  </a>
  
    <nav class="md-nav" aria-label="GroqProvider">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.providers.groq.GroqProvider.__init__" class="md-nav__link">
    <span class="md-ellipsis">
      __init__
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.providers.azure" class="md-nav__link">
    <span class="md-ellipsis">
      azure
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.providers.azure.AzureProvider" class="md-nav__link">
    <span class="md-ellipsis">
      AzureProvider
    </span>
  </a>
  
    <nav class="md-nav" aria-label="AzureProvider">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.providers.azure.AzureProvider.__init__" class="md-nav__link">
    <span class="md-ellipsis">
      __init__
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.providers.cohere" class="md-nav__link">
    <span class="md-ellipsis">
      cohere
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.providers.cohere.CohereProvider" class="md-nav__link">
    <span class="md-ellipsis">
      CohereProvider
    </span>
  </a>
  
    <nav class="md-nav" aria-label="CohereProvider">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.providers.cohere.CohereProvider.__init__" class="md-nav__link">
    <span class="md-ellipsis">
      __init__
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.providers.mistral" class="md-nav__link">
    <span class="md-ellipsis">
      mistral
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.providers.mistral.MistralProvider" class="md-nav__link">
    <span class="md-ellipsis">
      MistralProvider
    </span>
  </a>
  
    <nav class="md-nav" aria-label="MistralProvider">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.providers.mistral.MistralProvider.__init__" class="md-nav__link">
    <span class="md-ellipsis">
      __init__
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
    </ul>
  
</nav>
      
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../pydantic_graph/graph/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../pydantic_graph/nodes/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.nodes
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../pydantic_graph/persistence/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.persistence
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../pydantic_graph/mermaid/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.mermaid
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../pydantic_graph/exceptions/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_graph.exceptions
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../pydantic_evals/dataset/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.dataset
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../pydantic_evals/evaluators/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.evaluators
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../pydantic_evals/reporting/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.reporting
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../pydantic_evals/otel/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_evals.otel
    
  </span>
  

      </a>
    </li>
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../pydantic_evals/generation/" class="md-nav__link">
        
  
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
  <a href="#pydantic_ai.providers.Provider" class="md-nav__link">
    <span class="md-ellipsis">
      Provider
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.providers.Provider.name" class="md-nav__link">
    <span class="md-ellipsis">
      name
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.providers.Provider.base_url" class="md-nav__link">
    <span class="md-ellipsis">
      base_url
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.providers.Provider.client" class="md-nav__link">
    <span class="md-ellipsis">
      client
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.providers.google_vertex" class="md-nav__link">
    <span class="md-ellipsis">
      google_vertex
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.providers.google_vertex.GoogleVertexProvider" class="md-nav__link">
    <span class="md-ellipsis">
      GoogleVertexProvider
    </span>
  </a>
  
    <nav class="md-nav" aria-label="GoogleVertexProvider">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.providers.google_vertex.GoogleVertexProvider.__init__" class="md-nav__link">
    <span class="md-ellipsis">
      __init__
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.providers.openai" class="md-nav__link">
    <span class="md-ellipsis">
      openai
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.providers.openai.OpenAIProvider" class="md-nav__link">
    <span class="md-ellipsis">
      OpenAIProvider
    </span>
  </a>
  
    <nav class="md-nav" aria-label="OpenAIProvider">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.providers.openai.OpenAIProvider.__init__" class="md-nav__link">
    <span class="md-ellipsis">
      __init__
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.providers.deepseek" class="md-nav__link">
    <span class="md-ellipsis">
      deepseek
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.providers.deepseek.DeepSeekProvider" class="md-nav__link">
    <span class="md-ellipsis">
      DeepSeekProvider
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.providers.bedrock" class="md-nav__link">
    <span class="md-ellipsis">
      bedrock
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.providers.bedrock.BedrockProvider" class="md-nav__link">
    <span class="md-ellipsis">
      BedrockProvider
    </span>
  </a>
  
    <nav class="md-nav" aria-label="BedrockProvider">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.providers.bedrock.BedrockProvider.__init__" class="md-nav__link">
    <span class="md-ellipsis">
      __init__
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.providers.groq" class="md-nav__link">
    <span class="md-ellipsis">
      groq
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.providers.groq.GroqProvider" class="md-nav__link">
    <span class="md-ellipsis">
      GroqProvider
    </span>
  </a>
  
    <nav class="md-nav" aria-label="GroqProvider">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.providers.groq.GroqProvider.__init__" class="md-nav__link">
    <span class="md-ellipsis">
      __init__
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.providers.azure" class="md-nav__link">
    <span class="md-ellipsis">
      azure
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.providers.azure.AzureProvider" class="md-nav__link">
    <span class="md-ellipsis">
      AzureProvider
    </span>
  </a>
  
    <nav class="md-nav" aria-label="AzureProvider">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.providers.azure.AzureProvider.__init__" class="md-nav__link">
    <span class="md-ellipsis">
      __init__
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.providers.cohere" class="md-nav__link">
    <span class="md-ellipsis">
      cohere
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.providers.cohere.CohereProvider" class="md-nav__link">
    <span class="md-ellipsis">
      CohereProvider
    </span>
  </a>
  
    <nav class="md-nav" aria-label="CohereProvider">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.providers.cohere.CohereProvider.__init__" class="md-nav__link">
    <span class="md-ellipsis">
      __init__
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.providers.mistral" class="md-nav__link">
    <span class="md-ellipsis">
      mistral
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.providers.mistral.MistralProvider" class="md-nav__link">
    <span class="md-ellipsis">
      MistralProvider
    </span>
  </a>
  
    <nav class="md-nav" aria-label="MistralProvider">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.providers.mistral.MistralProvider.__init__" class="md-nav__link">
    <span class="md-ellipsis">
      __init__
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
            
          
          
            <div class="md-content" data-md-component="content">
              <article class="md-content__inner md-typeset">
                
                  


  
  


<h1 id="pydantic_aiproviders"><code>pydantic_ai.providers</code></h1>


<div class="doc doc-object doc-class">



<a id="pydantic_ai.providers.Provider"></a>
    <div class="doc doc-contents first">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-external" title="abc.ABC" href="https://docs.python.org/3/library/abc.html#abc.ABC">ABC</a></code>, <code><a class="autorefs autorefs-external" title="typing.Generic" href="https://docs.python.org/3/library/typing.html#typing.Generic">Generic</a>[<span title="pydantic_ai.providers.InterfaceClient">InterfaceClient</span>]</code></p>


        <p>Abstract class for a provider.</p>
<p>The provider is in charge of providing an authenticated client to the API.</p>
<p>Each provider only supports a specific interface. A interface can be supported by multiple providers.</p>
<p>For example, the OpenAIModel interface can be supported by the OpenAIProvider and the DeepSeekProvider.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/providers/__init__.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">14</span>
<span class="normal">15</span>
<span class="normal">16</span>
<span class="normal">17</span>
<span class="normal">18</span>
<span class="normal">19</span>
<span class="normal">20</span>
<span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span></pre></div></td><td class="code"><div><pre id="__code_0"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_0 > code"></button><code><span class="k">class</span><span class="w"> </span><span class="nc">Provider</span><span class="p">(</span><span class="n">ABC</span><span class="p">,</span> <span class="n">Generic</span><span class="p">[</span><span class="n">InterfaceClient</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""Abstract class for a provider.</span>

<span class="sd">    The provider is in charge of providing an authenticated client to the API.</span>

<span class="sd">    Each provider only supports a specific interface. A interface can be supported by multiple providers.</span>

<span class="sd">    For example, the OpenAIModel interface can be supported by the OpenAIProvider and the DeepSeekProvider.</span>
<span class="sd">    """</span>

    <span class="n">_client</span><span class="p">:</span> <span class="n">InterfaceClient</span>

    <span class="nd">@property</span>
    <span class="nd">@abstractmethod</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""The provider name."""</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>

    <span class="nd">@property</span>
    <span class="nd">@abstractmethod</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">base_url</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""The base URL for the provider API."""</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>

    <span class="nd">@property</span>
    <span class="nd">@abstractmethod</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">InterfaceClient</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""The client for the provider."""</span>
        <span class="k">raise</span> <span class="ne">NotImplementedError</span><span class="p">()</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h3 id="pydantic_ai.providers.Provider.name" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">name</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-abstractmethod"><code>abstractmethod</code></small>
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

</h3>
<div class="language-python doc-signature highlight"><pre id="__code_1"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_1 > code"></button><code><span class="n">name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The provider name.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h3 id="pydantic_ai.providers.Provider.base_url" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">base_url</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-abstractmethod"><code>abstractmethod</code></small>
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

</h3>
<div class="language-python doc-signature highlight"><pre id="__code_2"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_2 > code"></button><code><span class="n">base_url</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The base URL for the provider API.</p>
    </div>

</div>






<div class="doc doc-object doc-attribute">



<h3 id="pydantic_ai.providers.Provider.client" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">client</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-abstractmethod"><code>abstractmethod</code></small>
      <small class="doc doc-label doc-label-property"><code>property</code></small>
  </span>

</h3>
<div class="language-python doc-signature highlight"><pre id="__code_3"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_3 > code"></button><code><span class="n">client</span><span class="p">:</span> <span class="n"><span title="pydantic_ai.providers.InterfaceClient">InterfaceClient</span></span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>The client for the provider.</p>
    </div>

</div>




  </div>

    </div>

</div>

<div class="doc doc-object doc-module">



<a id="pydantic_ai.providers.google_vertex"></a>
    <div class="doc doc-contents first">








  <div class="doc doc-children">



















<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.providers.google_vertex.GoogleVertexProvider" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">GoogleVertexProvider</span>


</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-internal" title="pydantic_ai.providers.Provider" href="#pydantic_ai.providers.Provider">Provider</a>[<span title="httpx.AsyncClient">AsyncClient</span>]</code></p>


        <p>Provider for Vertex AI API.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/providers/google_vertex.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 30</span>
<span class="normal"> 31</span>
<span class="normal"> 32</span>
<span class="normal"> 33</span>
<span class="normal"> 34</span>
<span class="normal"> 35</span>
<span class="normal"> 36</span>
<span class="normal"> 37</span>
<span class="normal"> 38</span>
<span class="normal"> 39</span>
<span class="normal"> 40</span>
<span class="normal"> 41</span>
<span class="normal"> 42</span>
<span class="normal"> 43</span>
<span class="normal"> 44</span>
<span class="normal"> 45</span>
<span class="normal"> 46</span>
<span class="normal"> 47</span>
<span class="normal"> 48</span>
<span class="normal"> 49</span>
<span class="normal"> 50</span>
<span class="normal"> 51</span>
<span class="normal"> 52</span>
<span class="normal"> 53</span>
<span class="normal"> 54</span>
<span class="normal"> 55</span>
<span class="normal"> 56</span>
<span class="normal"> 57</span>
<span class="normal"> 58</span>
<span class="normal"> 59</span>
<span class="normal"> 60</span>
<span class="normal"> 61</span>
<span class="normal"> 62</span>
<span class="normal"> 63</span>
<span class="normal"> 64</span>
<span class="normal"> 65</span>
<span class="normal"> 66</span>
<span class="normal"> 67</span>
<span class="normal"> 68</span>
<span class="normal"> 69</span>
<span class="normal"> 70</span>
<span class="normal"> 71</span>
<span class="normal"> 72</span>
<span class="normal"> 73</span>
<span class="normal"> 74</span>
<span class="normal"> 75</span>
<span class="normal"> 76</span>
<span class="normal"> 77</span>
<span class="normal"> 78</span>
<span class="normal"> 79</span>
<span class="normal"> 80</span>
<span class="normal"> 81</span>
<span class="normal"> 82</span>
<span class="normal"> 83</span>
<span class="normal"> 84</span>
<span class="normal"> 85</span>
<span class="normal"> 86</span>
<span class="normal"> 87</span>
<span class="normal"> 88</span>
<span class="normal"> 89</span>
<span class="normal"> 90</span>
<span class="normal"> 91</span>
<span class="normal"> 92</span>
<span class="normal"> 93</span>
<span class="normal"> 94</span>
<span class="normal"> 95</span>
<span class="normal"> 96</span>
<span class="normal"> 97</span>
<span class="normal"> 98</span>
<span class="normal"> 99</span>
<span class="normal">100</span>
<span class="normal">101</span>
<span class="normal">102</span>
<span class="normal">103</span>
<span class="normal">104</span>
<span class="normal">105</span>
<span class="normal">106</span>
<span class="normal">107</span>
<span class="normal">108</span></pre></div></td><td class="code"><div><pre id="__code_4"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_4 > code"></button><code><span class="k">class</span><span class="w"> </span><span class="nc">GoogleVertexProvider</span><span class="p">(</span><span class="n">Provider</span><span class="p">[</span><span class="n">httpx</span><span class="o">.</span><span class="n">AsyncClient</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""Provider for Vertex AI API."""</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s1">'google-vertex'</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">base_url</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="p">(</span>
            <span class="sa">f</span><span class="s1">'https://</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">region</span><span class="si">}</span><span class="s1">-aiplatform.googleapis.com/v1'</span>
            <span class="sa">f</span><span class="s1">'/projects/</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">project_id</span><span class="si">}</span><span class="s1">'</span>
            <span class="sa">f</span><span class="s1">'/locations/</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">region</span><span class="si">}</span><span class="s1">'</span>
            <span class="sa">f</span><span class="s1">'/publishers/</span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">model_publisher</span><span class="si">}</span><span class="s1">/models/'</span>
        <span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">httpx</span><span class="o">.</span><span class="n">AsyncClient</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span>

    <span class="nd">@overload</span>
    <span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">service_account_file</span><span class="p">:</span> <span class="n">Path</span> <span class="o">|</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">project_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">region</span><span class="p">:</span> <span class="n">VertexAiRegion</span> <span class="o">=</span> <span class="s1">'us-central1'</span><span class="p">,</span>
        <span class="n">model_publisher</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">'google'</span><span class="p">,</span>
        <span class="n">http_client</span><span class="p">:</span> <span class="n">httpx</span><span class="o">.</span><span class="n">AsyncClient</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span> <span class="o">...</span>

    <span class="nd">@overload</span>
    <span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">service_account_info</span><span class="p">:</span> <span class="n">Mapping</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">project_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">region</span><span class="p">:</span> <span class="n">VertexAiRegion</span> <span class="o">=</span> <span class="s1">'us-central1'</span><span class="p">,</span>
        <span class="n">model_publisher</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">'google'</span><span class="p">,</span>
        <span class="n">http_client</span><span class="p">:</span> <span class="n">httpx</span><span class="o">.</span><span class="n">AsyncClient</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span> <span class="o">...</span>

    <span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">service_account_file</span><span class="p">:</span> <span class="n">Path</span> <span class="o">|</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">service_account_info</span><span class="p">:</span> <span class="n">Mapping</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">project_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">region</span><span class="p">:</span> <span class="n">VertexAiRegion</span> <span class="o">=</span> <span class="s1">'us-central1'</span><span class="p">,</span>
        <span class="n">model_publisher</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">'google'</span><span class="p">,</span>
        <span class="n">http_client</span><span class="p">:</span> <span class="n">httpx</span><span class="o">.</span><span class="n">AsyncClient</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create a new Vertex AI provider.</span>

<span class="sd">        Args:</span>
<span class="sd">            service_account_file: Path to a service account file.</span>
<span class="sd">                If not provided, the service_account_info or default environment credentials will be used.</span>
<span class="sd">            service_account_info: The loaded service_account_file contents.</span>
<span class="sd">                If not provided, the service_account_file or default environment credentials will be used.</span>
<span class="sd">            project_id: The project ID to use, if not provided it will be taken from the credentials.</span>
<span class="sd">            region: The region to make requests to.</span>
<span class="sd">            model_publisher: The model publisher to use, I couldn't find a good list of available publishers,</span>
<span class="sd">                and from trial and error it seems non-google models don't work with the `generateContent` and</span>
<span class="sd">                `streamGenerateContent` functions, hence only `google` is currently supported.</span>
<span class="sd">                Please create an issue or PR if you know how to use other publishers.</span>
<span class="sd">            http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">service_account_file</span> <span class="ow">and</span> <span class="n">service_account_info</span><span class="p">:</span>
            <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s1">'Only one of `service_account_file` or `service_account_info` can be provided.'</span><span class="p">)</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">http_client</span> <span class="ow">or</span> <span class="n">cached_async_http_client</span><span class="p">(</span><span class="n">provider</span><span class="o">=</span><span class="s1">'google-vertex'</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">service_account_file</span> <span class="o">=</span> <span class="n">service_account_file</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">service_account_info</span> <span class="o">=</span> <span class="n">service_account_info</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">project_id</span> <span class="o">=</span> <span class="n">project_id</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">region</span> <span class="o">=</span> <span class="n">region</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">model_publisher</span> <span class="o">=</span> <span class="n">model_publisher</span>

        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">auth</span> <span class="o">=</span> <span class="n">_VertexAIAuth</span><span class="p">(</span><span class="n">service_account_file</span><span class="p">,</span> <span class="n">service_account_info</span><span class="p">,</span> <span class="n">project_id</span><span class="p">,</span> <span class="n">region</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">base_url</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">base_url</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.providers.google_vertex.GoogleVertexProvider.__init__" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">__init__</span>


</h4>
          <div class="doc-overloads">
<div class="language-python doc-signature highlight"><pre id="__code_5"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_5 > code"></button><code><span class="fm">__init__</span><span class="p">(</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="nf">service_account_file</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="pathlib.Path" href="https://docs.python.org/3/library/pathlib.html#pathlib.Path">Path</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">project_id</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">region</span><span class="p">:</span> <span class="n"><span title="pydantic_ai.providers.google_vertex.VertexAiRegion">VertexAiRegion</span></span> <span class="o">=</span> <span class="s2">"us-central1"</span><span class="p">,</span>
    <span class="n">model_publisher</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">=</span> <span class="s2">"google"</span><span class="p">,</span>
    <span class="n">http_client</span><span class="p">:</span> <span class="n"><span title="httpx.AsyncClient">AsyncClient</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span>
</code></pre></div><div class="language-python doc-signature highlight"><pre id="__code_6"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_6 > code"></button><code><span class="fm">__init__</span><span class="p">(</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="nf">service_account_info</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Mapping" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping">Mapping</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">project_id</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">region</span><span class="p">:</span> <span class="n"><span title="pydantic_ai.providers.google_vertex.VertexAiRegion">VertexAiRegion</span></span> <span class="o">=</span> <span class="s2">"us-central1"</span><span class="p">,</span>
    <span class="n">model_publisher</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">=</span> <span class="s2">"google"</span><span class="p">,</span>
    <span class="n">http_client</span><span class="p">:</span> <span class="n"><span title="httpx.AsyncClient">AsyncClient</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span>
</code></pre></div>          </div>
<div class="language-python doc-signature highlight"><pre id="__code_7"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_7 > code"></button><code><span class="fm">__init__</span><span class="p">(</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="nf">service_account_file</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="pathlib.Path" href="https://docs.python.org/3/library/pathlib.html#pathlib.Path">Path</a></span> <span class="o">|</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">service_account_info</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="collections.abc.Mapping" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping">Mapping</a></span><span class="p">[</span><span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">,</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">project_id</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">region</span><span class="p">:</span> <span class="n"><span title="pydantic_ai.providers.google_vertex.VertexAiRegion">VertexAiRegion</span></span> <span class="o">=</span> <span class="s2">"us-central1"</span><span class="p">,</span>
    <span class="n">model_publisher</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">=</span> <span class="s2">"google"</span><span class="p">,</span>
    <span class="n">http_client</span><span class="p">:</span> <span class="n"><span title="httpx.AsyncClient">AsyncClient</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Create a new Vertex AI provider.</p>


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
                <code>service_account_file</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" title="pathlib.Path" href="https://docs.python.org/3/library/pathlib.html#pathlib.Path">Path</a> | <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>Path to a service account file.
If not provided, the service_account_info or default environment credentials will be used.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>service_account_info</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" title="collections.abc.Mapping" href="https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping">Mapping</a>[<a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a>, <a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a>] | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The loaded service_account_file contents.
If not provided, the service_account_file or default environment credentials will be used.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>project_id</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The project ID to use, if not provided it will be taken from the credentials.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>region</code>
            </td>
            <td>
                  <code><span title="pydantic_ai.providers.google_vertex.VertexAiRegion">VertexAiRegion</span></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The region to make requests to.</p>
              </div>
            </td>
            <td>
                  <code>'us-central1'</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>model_publisher</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The model publisher to use, I couldn't find a good list of available publishers,
and from trial and error it seems non-google models don't work with the <code>generateContent</code> and
<code>streamGenerateContent</code> functions, hence only <code>google</code> is currently supported.
Please create an issue or PR if you know how to use other publishers.</p>
              </div>
            </td>
            <td>
                  <code>'google'</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>http_client</code>
            </td>
            <td>
                  <code><span title="httpx.AsyncClient">AsyncClient</span> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>An existing <code>httpx.AsyncClient</code> to use for making HTTP requests.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/providers/google_vertex.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 72</span>
<span class="normal"> 73</span>
<span class="normal"> 74</span>
<span class="normal"> 75</span>
<span class="normal"> 76</span>
<span class="normal"> 77</span>
<span class="normal"> 78</span>
<span class="normal"> 79</span>
<span class="normal"> 80</span>
<span class="normal"> 81</span>
<span class="normal"> 82</span>
<span class="normal"> 83</span>
<span class="normal"> 84</span>
<span class="normal"> 85</span>
<span class="normal"> 86</span>
<span class="normal"> 87</span>
<span class="normal"> 88</span>
<span class="normal"> 89</span>
<span class="normal"> 90</span>
<span class="normal"> 91</span>
<span class="normal"> 92</span>
<span class="normal"> 93</span>
<span class="normal"> 94</span>
<span class="normal"> 95</span>
<span class="normal"> 96</span>
<span class="normal"> 97</span>
<span class="normal"> 98</span>
<span class="normal"> 99</span>
<span class="normal">100</span>
<span class="normal">101</span>
<span class="normal">102</span>
<span class="normal">103</span>
<span class="normal">104</span>
<span class="normal">105</span>
<span class="normal">106</span>
<span class="normal">107</span>
<span class="normal">108</span></pre></div></td><td class="code"><div><pre id="__code_8"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_8 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">service_account_file</span><span class="p">:</span> <span class="n">Path</span> <span class="o">|</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">service_account_info</span><span class="p">:</span> <span class="n">Mapping</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="nb">str</span><span class="p">]</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">project_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">region</span><span class="p">:</span> <span class="n">VertexAiRegion</span> <span class="o">=</span> <span class="s1">'us-central1'</span><span class="p">,</span>
    <span class="n">model_publisher</span><span class="p">:</span> <span class="nb">str</span> <span class="o">=</span> <span class="s1">'google'</span><span class="p">,</span>
    <span class="n">http_client</span><span class="p">:</span> <span class="n">httpx</span><span class="o">.</span><span class="n">AsyncClient</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create a new Vertex AI provider.</span>

<span class="sd">    Args:</span>
<span class="sd">        service_account_file: Path to a service account file.</span>
<span class="sd">            If not provided, the service_account_info or default environment credentials will be used.</span>
<span class="sd">        service_account_info: The loaded service_account_file contents.</span>
<span class="sd">            If not provided, the service_account_file or default environment credentials will be used.</span>
<span class="sd">        project_id: The project ID to use, if not provided it will be taken from the credentials.</span>
<span class="sd">        region: The region to make requests to.</span>
<span class="sd">        model_publisher: The model publisher to use, I couldn't find a good list of available publishers,</span>
<span class="sd">            and from trial and error it seems non-google models don't work with the `generateContent` and</span>
<span class="sd">            `streamGenerateContent` functions, hence only `google` is currently supported.</span>
<span class="sd">            Please create an issue or PR if you know how to use other publishers.</span>
<span class="sd">        http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">service_account_file</span> <span class="ow">and</span> <span class="n">service_account_info</span><span class="p">:</span>
        <span class="k">raise</span> <span class="ne">ValueError</span><span class="p">(</span><span class="s1">'Only one of `service_account_file` or `service_account_info` can be provided.'</span><span class="p">)</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">http_client</span> <span class="ow">or</span> <span class="n">cached_async_http_client</span><span class="p">(</span><span class="n">provider</span><span class="o">=</span><span class="s1">'google-vertex'</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">service_account_file</span> <span class="o">=</span> <span class="n">service_account_file</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">service_account_info</span> <span class="o">=</span> <span class="n">service_account_info</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">project_id</span> <span class="o">=</span> <span class="n">project_id</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">region</span> <span class="o">=</span> <span class="n">region</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">model_publisher</span> <span class="o">=</span> <span class="n">model_publisher</span>

    <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">auth</span> <span class="o">=</span> <span class="n">_VertexAIAuth</span><span class="p">(</span><span class="n">service_account_file</span><span class="p">,</span> <span class="n">service_account_info</span><span class="p">,</span> <span class="n">project_id</span><span class="p">,</span> <span class="n">region</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">base_url</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">base_url</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>




  </div>

    </div>

</div>












  </div>

    </div>

</div>

<div class="doc doc-object doc-module">



<a id="pydantic_ai.providers.openai"></a>
    <div class="doc doc-contents first">








  <div class="doc doc-children">















<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.providers.openai.OpenAIProvider" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">OpenAIProvider</span>


</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-internal" title="pydantic_ai.providers.Provider" href="#pydantic_ai.providers.Provider">Provider</a>[<span title="openai.AsyncOpenAI">AsyncOpenAI</span>]</code></p>


        <p>Provider for OpenAI API.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/providers/openai.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">19</span>
<span class="normal">20</span>
<span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span></pre></div></td><td class="code"><div><pre id="__code_9"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_9 > code"></button><code tabindex="0"><span class="k">class</span><span class="w"> </span><span class="nc">OpenAIProvider</span><span class="p">(</span><span class="n">Provider</span><span class="p">[</span><span class="n">AsyncOpenAI</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""Provider for OpenAI API."""</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s1">'openai'</span>  <span class="c1"># pragma: no cover</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">base_url</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">base_url</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncOpenAI</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span>

    <span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">base_url</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">openai_client</span><span class="p">:</span> <span class="n">AsyncOpenAI</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">http_client</span><span class="p">:</span> <span class="n">httpx</span><span class="o">.</span><span class="n">AsyncClient</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create a new OpenAI provider.</span>

<span class="sd">        Args:</span>
<span class="sd">            base_url: The base url for the OpenAI requests. If not provided, the `OPENAI_BASE_URL` environment variable</span>
<span class="sd">                will be used if available. Otherwise, defaults to OpenAI's base url.</span>
<span class="sd">            api_key: The API key to use for authentication, if not provided, the `OPENAI_API_KEY` environment variable</span>
<span class="sd">                will be used if available.</span>
<span class="sd">            openai_client: An existing</span>
<span class="sd">                [`AsyncOpenAI`](https://github.com/openai/openai-python?tab=readme-ov-file#async-usage)</span>
<span class="sd">                client to use. If provided, `base_url`, `api_key`, and `http_client` must be `None`.</span>
<span class="sd">            http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.</span>
<span class="sd">        """</span>
        <span class="c1"># This is a workaround for the OpenAI client requiring an API key, whilst locally served,</span>
        <span class="c1"># openai compatible models do not always need an API key, but a placeholder (non-empty) key is required.</span>
        <span class="k">if</span> <span class="n">api_key</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="s1">'OPENAI_API_KEY'</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span> <span class="ow">and</span> <span class="n">base_url</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">openai_client</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="n">api_key</span> <span class="o">=</span> <span class="s1">'api-key-not-set'</span>

        <span class="k">if</span> <span class="n">openai_client</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">assert</span> <span class="n">base_url</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'Cannot provide both `openai_client` and `base_url`'</span>
            <span class="k">assert</span> <span class="n">http_client</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'Cannot provide both `openai_client` and `http_client`'</span>
            <span class="k">assert</span> <span class="n">api_key</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'Cannot provide both `openai_client` and `api_key`'</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">openai_client</span>
        <span class="k">elif</span> <span class="n">http_client</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">AsyncOpenAI</span><span class="p">(</span><span class="n">base_url</span><span class="o">=</span><span class="n">base_url</span><span class="p">,</span> <span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">,</span> <span class="n">http_client</span><span class="o">=</span><span class="n">http_client</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">http_client</span> <span class="o">=</span> <span class="n">cached_async_http_client</span><span class="p">(</span><span class="n">provider</span><span class="o">=</span><span class="s1">'openai'</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">AsyncOpenAI</span><span class="p">(</span><span class="n">base_url</span><span class="o">=</span><span class="n">base_url</span><span class="p">,</span> <span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">,</span> <span class="n">http_client</span><span class="o">=</span><span class="n">http_client</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.providers.openai.OpenAIProvider.__init__" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">__init__</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_10"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_10 > code"></button><code><span class="fm">__init__</span><span class="p">(</span>
    <span class="nf">base_url</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">api_key</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">openai_client</span><span class="p">:</span> <span class="n"><span title="openai.AsyncOpenAI">AsyncOpenAI</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">http_client</span><span class="p">:</span> <span class="n"><span title="httpx.AsyncClient">AsyncClient</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Create a new OpenAI provider.</p>


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
                <code>base_url</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The base url for the OpenAI requests. If not provided, the <code>OPENAI_BASE_URL</code> environment variable
will be used if available. Otherwise, defaults to OpenAI's base url.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>api_key</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The API key to use for authentication, if not provided, the <code>OPENAI_API_KEY</code> environment variable
will be used if available.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>openai_client</code>
            </td>
            <td>
                  <code><span title="openai.AsyncOpenAI">AsyncOpenAI</span> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>An existing
<a href="https://github.com/openai/openai-python?tab=readme-ov-file#async-usage"><code>AsyncOpenAI</code></a>
client to use. If provided, <code>base_url</code>, <code>api_key</code>, and <code>http_client</code> must be <code>None</code>.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>http_client</code>
            </td>
            <td>
                  <code><span title="httpx.AsyncClient">AsyncClient</span> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>An existing <code>httpx.AsyncClient</code> to use for making HTTP requests.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/providers/openai.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span></pre></div></td><td class="code"><div><pre id="__code_11"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_11 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="n">base_url</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">openai_client</span><span class="p">:</span> <span class="n">AsyncOpenAI</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">http_client</span><span class="p">:</span> <span class="n">httpx</span><span class="o">.</span><span class="n">AsyncClient</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create a new OpenAI provider.</span>

<span class="sd">    Args:</span>
<span class="sd">        base_url: The base url for the OpenAI requests. If not provided, the `OPENAI_BASE_URL` environment variable</span>
<span class="sd">            will be used if available. Otherwise, defaults to OpenAI's base url.</span>
<span class="sd">        api_key: The API key to use for authentication, if not provided, the `OPENAI_API_KEY` environment variable</span>
<span class="sd">            will be used if available.</span>
<span class="sd">        openai_client: An existing</span>
<span class="sd">            [`AsyncOpenAI`](https://github.com/openai/openai-python?tab=readme-ov-file#async-usage)</span>
<span class="sd">            client to use. If provided, `base_url`, `api_key`, and `http_client` must be `None`.</span>
<span class="sd">        http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.</span>
<span class="sd">    """</span>
    <span class="c1"># This is a workaround for the OpenAI client requiring an API key, whilst locally served,</span>
    <span class="c1"># openai compatible models do not always need an API key, but a placeholder (non-empty) key is required.</span>
    <span class="k">if</span> <span class="n">api_key</span> <span class="ow">is</span> <span class="kc">None</span> <span class="ow">and</span> <span class="s1">'OPENAI_API_KEY'</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span> <span class="ow">and</span> <span class="n">base_url</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span> <span class="ow">and</span> <span class="n">openai_client</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">api_key</span> <span class="o">=</span> <span class="s1">'api-key-not-set'</span>

    <span class="k">if</span> <span class="n">openai_client</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">assert</span> <span class="n">base_url</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'Cannot provide both `openai_client` and `base_url`'</span>
        <span class="k">assert</span> <span class="n">http_client</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'Cannot provide both `openai_client` and `http_client`'</span>
        <span class="k">assert</span> <span class="n">api_key</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'Cannot provide both `openai_client` and `api_key`'</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">openai_client</span>
    <span class="k">elif</span> <span class="n">http_client</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">AsyncOpenAI</span><span class="p">(</span><span class="n">base_url</span><span class="o">=</span><span class="n">base_url</span><span class="p">,</span> <span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">,</span> <span class="n">http_client</span><span class="o">=</span><span class="n">http_client</span><span class="p">)</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">http_client</span> <span class="o">=</span> <span class="n">cached_async_http_client</span><span class="p">(</span><span class="n">provider</span><span class="o">=</span><span class="s1">'openai'</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">AsyncOpenAI</span><span class="p">(</span><span class="n">base_url</span><span class="o">=</span><span class="n">base_url</span><span class="p">,</span> <span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">,</span> <span class="n">http_client</span><span class="o">=</span><span class="n">http_client</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>




  </div>

    </div>

</div>




  </div>

    </div>

</div>

<div class="doc doc-object doc-module">



<a id="pydantic_ai.providers.deepseek"></a>
    <div class="doc doc-contents first">








  <div class="doc doc-children">



















<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.providers.deepseek.DeepSeekProvider" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">DeepSeekProvider</span>


</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-internal" title="pydantic_ai.providers.Provider" href="#pydantic_ai.providers.Provider">Provider</a>[<span title="openai.AsyncOpenAI">AsyncOpenAI</span>]</code></p>


        <p>Provider for DeepSeek API.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/providers/deepseek.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span></pre></div></td><td class="code"><div><pre id="__code_12"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_12 > code"></button><code tabindex="0"><span class="k">class</span><span class="w"> </span><span class="nc">DeepSeekProvider</span><span class="p">(</span><span class="n">Provider</span><span class="p">[</span><span class="n">AsyncOpenAI</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""Provider for DeepSeek API."""</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s1">'deepseek'</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">base_url</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s1">'https://api.deepseek.com'</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncOpenAI</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span>

    <span class="nd">@overload</span>
    <span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span> <span class="o">...</span>

    <span class="nd">@overload</span>
    <span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span> <span class="o">...</span>

    <span class="nd">@overload</span>
    <span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span><span class="p">,</span> <span class="n">http_client</span><span class="p">:</span> <span class="n">AsyncHTTPClient</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span> <span class="o">...</span>

    <span class="nd">@overload</span>
    <span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">openai_client</span><span class="p">:</span> <span class="n">AsyncOpenAI</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span> <span class="o">...</span>

    <span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">openai_client</span><span class="p">:</span> <span class="n">AsyncOpenAI</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">http_client</span><span class="p">:</span> <span class="n">AsyncHTTPClient</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="n">api_key</span> <span class="o">=</span> <span class="n">api_key</span> <span class="ow">or</span> <span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="s1">'DEEPSEEK_API_KEY'</span><span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">api_key</span> <span class="ow">and</span> <span class="n">openai_client</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">raise</span> <span class="n">UserError</span><span class="p">(</span>
                <span class="s1">'Set the `DEEPSEEK_API_KEY` environment variable or pass it via `DeepSeekProvider(api_key=...)`'</span>
                <span class="s1">'to use the DeepSeek provider.'</span>
            <span class="p">)</span>

        <span class="k">if</span> <span class="n">openai_client</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">openai_client</span>
        <span class="k">elif</span> <span class="n">http_client</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">AsyncOpenAI</span><span class="p">(</span><span class="n">base_url</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">base_url</span><span class="p">,</span> <span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">,</span> <span class="n">http_client</span><span class="o">=</span><span class="n">http_client</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">http_client</span> <span class="o">=</span> <span class="n">cached_async_http_client</span><span class="p">(</span><span class="n">provider</span><span class="o">=</span><span class="s1">'deepseek'</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">AsyncOpenAI</span><span class="p">(</span><span class="n">base_url</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">base_url</span><span class="p">,</span> <span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">,</span> <span class="n">http_client</span><span class="o">=</span><span class="n">http_client</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">





  </div>

    </div>

</div>




  </div>

    </div>

</div>

<div class="doc doc-object doc-module">



<a id="pydantic_ai.providers.bedrock"></a>
    <div class="doc doc-contents first">








  <div class="doc doc-children">















<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.providers.bedrock.BedrockProvider" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">BedrockProvider</span>


</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-internal" title="pydantic_ai.providers.Provider" href="#pydantic_ai.providers.Provider">Provider</a>[<span title="botocore.client.BaseClient">BaseClient</span>]</code></p>


        <p>Provider for AWS Bedrock.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/providers/bedrock.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span></pre></div></td><td class="code"><div><pre id="__code_13"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_13 > code"></button><code tabindex="0"><span class="k">class</span><span class="w"> </span><span class="nc">BedrockProvider</span><span class="p">(</span><span class="n">Provider</span><span class="p">[</span><span class="n">BaseClient</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""Provider for AWS Bedrock."""</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s1">'bedrock'</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">base_url</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">meta</span><span class="o">.</span><span class="n">endpoint_url</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">BaseClient</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span>

    <span class="nd">@overload</span>
    <span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">bedrock_client</span><span class="p">:</span> <span class="n">BaseClient</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span> <span class="o">...</span>

    <span class="nd">@overload</span>
    <span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">region_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">aws_access_key_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">aws_secret_access_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">aws_session_token</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">aws_read_timeout</span><span class="p">:</span> <span class="nb">float</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">aws_connect_timeout</span><span class="p">:</span> <span class="nb">float</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span> <span class="o">...</span>

    <span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">bedrock_client</span><span class="p">:</span> <span class="n">BaseClient</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">region_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">aws_access_key_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">aws_secret_access_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">aws_session_token</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">aws_read_timeout</span><span class="p">:</span> <span class="nb">float</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">aws_connect_timeout</span><span class="p">:</span> <span class="nb">float</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Initialize the Bedrock provider.</span>

<span class="sd">        Args:</span>
<span class="sd">            bedrock_client: A boto3 client for Bedrock Runtime. If provided, other arguments are ignored.</span>
<span class="sd">            region_name: The AWS region name.</span>
<span class="sd">            aws_access_key_id: The AWS access key ID.</span>
<span class="sd">            aws_secret_access_key: The AWS secret access key.</span>
<span class="sd">            aws_session_token: The AWS session token.</span>
<span class="sd">            aws_read_timeout: The read timeout for Bedrock client.</span>
<span class="sd">            aws_connect_timeout: The connect timeout for Bedrock client.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">bedrock_client</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">bedrock_client</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">read_timeout</span> <span class="o">=</span> <span class="n">aws_read_timeout</span> <span class="ow">or</span> <span class="nb">float</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="s1">'AWS_READ_TIMEOUT'</span><span class="p">,</span> <span class="mi">300</span><span class="p">))</span>
                <span class="n">connect_timeout</span> <span class="o">=</span> <span class="n">aws_connect_timeout</span> <span class="ow">or</span> <span class="nb">float</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="s1">'AWS_CONNECT_TIMEOUT'</span><span class="p">,</span> <span class="mi">60</span><span class="p">))</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">boto3</span><span class="o">.</span><span class="n">client</span><span class="p">(</span>  <span class="c1"># type: ignore[reportUnknownMemberType]</span>
                    <span class="s1">'bedrock-runtime'</span><span class="p">,</span>
                    <span class="n">aws_access_key_id</span><span class="o">=</span><span class="n">aws_access_key_id</span><span class="p">,</span>
                    <span class="n">aws_secret_access_key</span><span class="o">=</span><span class="n">aws_secret_access_key</span><span class="p">,</span>
                    <span class="n">aws_session_token</span><span class="o">=</span><span class="n">aws_session_token</span><span class="p">,</span>
                    <span class="n">region_name</span><span class="o">=</span><span class="n">region_name</span><span class="p">,</span>
                    <span class="n">config</span><span class="o">=</span><span class="n">Config</span><span class="p">(</span><span class="n">read_timeout</span><span class="o">=</span><span class="n">read_timeout</span><span class="p">,</span> <span class="n">connect_timeout</span><span class="o">=</span><span class="n">connect_timeout</span><span class="p">),</span>
                <span class="p">)</span>
            <span class="k">except</span> <span class="n">NoRegionError</span> <span class="k">as</span> <span class="n">exc</span><span class="p">:</span>  <span class="c1"># pragma: no cover</span>
                <span class="k">raise</span> <span class="n">UserError</span><span class="p">(</span><span class="s1">'You must provide a `region_name` or a boto3 client for Bedrock Runtime.'</span><span class="p">)</span> <span class="kn">from</span><span class="w"> </span><span class="nn">exc</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.providers.bedrock.BedrockProvider.__init__" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">__init__</span>


</h4>
          <div class="doc-overloads">
<div class="language-python doc-signature highlight"><pre id="__code_14"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_14 > code"></button><code><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="p">,</span> <span class="nf">bedrock_client</span><span class="p">:</span> <span class="n"><span title="botocore.client.BaseClient">BaseClient</span></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span>
</code></pre></div><div class="language-python doc-signature highlight"><pre id="__code_15"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_15 > code"></button><code><span class="fm">__init__</span><span class="p">(</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="nf">region_name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">aws_access_key_id</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">aws_secret_access_key</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">aws_session_token</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">aws_read_timeout</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#float">float</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">aws_connect_timeout</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#float">float</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span>
</code></pre></div>          </div>
<div class="language-python doc-signature highlight"><pre id="__code_16"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_16 > code"></button><code><span class="fm">__init__</span><span class="p">(</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="nf">bedrock_client</span><span class="p">:</span> <span class="n"><span title="botocore.client.BaseClient">BaseClient</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">region_name</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">aws_access_key_id</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">aws_secret_access_key</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">aws_session_token</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">aws_read_timeout</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#float">float</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">aws_connect_timeout</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#float">float</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Initialize the Bedrock provider.</p>


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
                <code>bedrock_client</code>
            </td>
            <td>
                  <code><span title="botocore.client.BaseClient">BaseClient</span> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>A boto3 client for Bedrock Runtime. If provided, other arguments are ignored.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>region_name</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The AWS region name.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>aws_access_key_id</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The AWS access key ID.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>aws_secret_access_key</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The AWS secret access key.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>aws_session_token</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The AWS session token.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>aws_read_timeout</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#float">float</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The read timeout for Bedrock client.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>aws_connect_timeout</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/functions.html#float">float</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The connect timeout for Bedrock client.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/providers/bedrock.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span>
<span class="normal">76</span>
<span class="normal">77</span>
<span class="normal">78</span>
<span class="normal">79</span>
<span class="normal">80</span>
<span class="normal">81</span>
<span class="normal">82</span>
<span class="normal">83</span>
<span class="normal">84</span>
<span class="normal">85</span>
<span class="normal">86</span>
<span class="normal">87</span>
<span class="normal">88</span></pre></div></td><td class="code"><div><pre id="__code_17"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_17 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">bedrock_client</span><span class="p">:</span> <span class="n">BaseClient</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">region_name</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">aws_access_key_id</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">aws_secret_access_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">aws_session_token</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">aws_read_timeout</span><span class="p">:</span> <span class="nb">float</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">aws_connect_timeout</span><span class="p">:</span> <span class="nb">float</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Initialize the Bedrock provider.</span>

<span class="sd">    Args:</span>
<span class="sd">        bedrock_client: A boto3 client for Bedrock Runtime. If provided, other arguments are ignored.</span>
<span class="sd">        region_name: The AWS region name.</span>
<span class="sd">        aws_access_key_id: The AWS access key ID.</span>
<span class="sd">        aws_secret_access_key: The AWS secret access key.</span>
<span class="sd">        aws_session_token: The AWS session token.</span>
<span class="sd">        aws_read_timeout: The read timeout for Bedrock client.</span>
<span class="sd">        aws_connect_timeout: The connect timeout for Bedrock client.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">bedrock_client</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">bedrock_client</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="n">read_timeout</span> <span class="o">=</span> <span class="n">aws_read_timeout</span> <span class="ow">or</span> <span class="nb">float</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="s1">'AWS_READ_TIMEOUT'</span><span class="p">,</span> <span class="mi">300</span><span class="p">))</span>
            <span class="n">connect_timeout</span> <span class="o">=</span> <span class="n">aws_connect_timeout</span> <span class="ow">or</span> <span class="nb">float</span><span class="p">(</span><span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="s1">'AWS_CONNECT_TIMEOUT'</span><span class="p">,</span> <span class="mi">60</span><span class="p">))</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">boto3</span><span class="o">.</span><span class="n">client</span><span class="p">(</span>  <span class="c1"># type: ignore[reportUnknownMemberType]</span>
                <span class="s1">'bedrock-runtime'</span><span class="p">,</span>
                <span class="n">aws_access_key_id</span><span class="o">=</span><span class="n">aws_access_key_id</span><span class="p">,</span>
                <span class="n">aws_secret_access_key</span><span class="o">=</span><span class="n">aws_secret_access_key</span><span class="p">,</span>
                <span class="n">aws_session_token</span><span class="o">=</span><span class="n">aws_session_token</span><span class="p">,</span>
                <span class="n">region_name</span><span class="o">=</span><span class="n">region_name</span><span class="p">,</span>
                <span class="n">config</span><span class="o">=</span><span class="n">Config</span><span class="p">(</span><span class="n">read_timeout</span><span class="o">=</span><span class="n">read_timeout</span><span class="p">,</span> <span class="n">connect_timeout</span><span class="o">=</span><span class="n">connect_timeout</span><span class="p">),</span>
            <span class="p">)</span>
        <span class="k">except</span> <span class="n">NoRegionError</span> <span class="k">as</span> <span class="n">exc</span><span class="p">:</span>  <span class="c1"># pragma: no cover</span>
            <span class="k">raise</span> <span class="n">UserError</span><span class="p">(</span><span class="s1">'You must provide a `region_name` or a boto3 client for Bedrock Runtime.'</span><span class="p">)</span> <span class="kn">from</span><span class="w"> </span><span class="nn">exc</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>




  </div>

    </div>

</div>




  </div>

    </div>

</div>

<div class="doc doc-object doc-module">



<a id="pydantic_ai.providers.groq"></a>
    <div class="doc doc-contents first">








  <div class="doc doc-children">



















<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.providers.groq.GroqProvider" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">GroqProvider</span>


</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-internal" title="pydantic_ai.providers.Provider" href="#pydantic_ai.providers.Provider">Provider</a>[<span title="groq.AsyncGroq">AsyncGroq</span>]</code></p>


        <p>Provider for Groq API.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/providers/groq.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span></pre></div></td><td class="code"><div><pre id="__code_18"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_18 > code"></button><code tabindex="0"><span class="k">class</span><span class="w"> </span><span class="nc">GroqProvider</span><span class="p">(</span><span class="n">Provider</span><span class="p">[</span><span class="n">AsyncGroq</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""Provider for Groq API."""</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s1">'groq'</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">base_url</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'GROQ_BASE_URL'</span><span class="p">,</span> <span class="s1">'https://api.groq.com'</span><span class="p">)</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncGroq</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span>

    <span class="nd">@overload</span>
    <span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">groq_client</span><span class="p">:</span> <span class="n">AsyncGroq</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span> <span class="o">...</span>

    <span class="nd">@overload</span>
    <span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">http_client</span><span class="p">:</span> <span class="n">AsyncHTTPClient</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span> <span class="o">...</span>

    <span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">groq_client</span><span class="p">:</span> <span class="n">AsyncGroq</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">http_client</span><span class="p">:</span> <span class="n">AsyncHTTPClient</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create a new Groq provider.</span>

<span class="sd">        Args:</span>
<span class="sd">            api_key: The API key to use for authentication, if not provided, the `GROQ_API_KEY` environment variable</span>
<span class="sd">                will be used if available.</span>
<span class="sd">            groq_client: An existing</span>
<span class="sd">                [`AsyncGroq`](https://github.com/groq/groq-python?tab=readme-ov-file#async-usage)</span>
<span class="sd">                client to use. If provided, `api_key` and `http_client` must be `None`.</span>
<span class="sd">            http_client: An existing `AsyncHTTPClient` to use for making HTTP requests.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">groq_client</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">assert</span> <span class="n">http_client</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'Cannot provide both `groq_client` and `http_client`'</span>
            <span class="k">assert</span> <span class="n">api_key</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'Cannot provide both `groq_client` and `api_key`'</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">groq_client</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">api_key</span> <span class="o">=</span> <span class="n">api_key</span> <span class="ow">or</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'GROQ_API_KEY'</span><span class="p">)</span>

            <span class="k">if</span> <span class="ow">not</span> <span class="n">api_key</span><span class="p">:</span>
                <span class="k">raise</span> <span class="n">UserError</span><span class="p">(</span>
                    <span class="s1">'Set the `GROQ_API_KEY` environment variable or pass it via `GroqProvider(api_key=...)`'</span>
                    <span class="s1">'to use the Groq provider.'</span>
                <span class="p">)</span>
            <span class="k">elif</span> <span class="n">http_client</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">AsyncGroq</span><span class="p">(</span><span class="n">base_url</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">base_url</span><span class="p">,</span> <span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">,</span> <span class="n">http_client</span><span class="o">=</span><span class="n">http_client</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">http_client</span> <span class="o">=</span> <span class="n">cached_async_http_client</span><span class="p">(</span><span class="n">provider</span><span class="o">=</span><span class="s1">'groq'</span><span class="p">)</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">AsyncGroq</span><span class="p">(</span><span class="n">base_url</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">base_url</span><span class="p">,</span> <span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">,</span> <span class="n">http_client</span><span class="o">=</span><span class="n">http_client</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.providers.groq.GroqProvider.__init__" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">__init__</span>


</h4>
          <div class="doc-overloads">
<div class="language-python doc-signature highlight"><pre id="__code_19"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_19 > code"></button><code><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="p">,</span> <span class="nf">groq_client</span><span class="p">:</span> <span class="n"><span title="groq.AsyncGroq">AsyncGroq</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span>
</code></pre></div><div class="language-python doc-signature highlight"><pre id="__code_20"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_20 > code"></button><code><span class="fm">__init__</span><span class="p">(</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="nf">api_key</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">http_client</span><span class="p">:</span> <span class="n"><span title="httpx.AsyncClient">AsyncClient</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span>
</code></pre></div>          </div>
<div class="language-python doc-signature highlight"><pre id="__code_21"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_21 > code"></button><code><span class="fm">__init__</span><span class="p">(</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="nf">api_key</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">groq_client</span><span class="p">:</span> <span class="n"><span title="groq.AsyncGroq">AsyncGroq</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">http_client</span><span class="p">:</span> <span class="n"><span title="httpx.AsyncClient">AsyncClient</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Create a new Groq provider.</p>


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
                <code>api_key</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The API key to use for authentication, if not provided, the <code>GROQ_API_KEY</code> environment variable
will be used if available.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>groq_client</code>
            </td>
            <td>
                  <code><span title="groq.AsyncGroq">AsyncGroq</span> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>An existing
<a href="https://github.com/groq/groq-python?tab=readme-ov-file#async-usage"><code>AsyncGroq</code></a>
client to use. If provided, <code>api_key</code> and <code>http_client</code> must be <code>None</code>.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>http_client</code>
            </td>
            <td>
                  <code><span title="httpx.AsyncClient">AsyncClient</span> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>An existing <code>AsyncHTTPClient</code> to use for making HTTP requests.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/providers/groq.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span>
<span class="normal">74</span>
<span class="normal">75</span></pre></div></td><td class="code"><div><pre id="__code_22"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_22 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">groq_client</span><span class="p">:</span> <span class="n">AsyncGroq</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">http_client</span><span class="p">:</span> <span class="n">AsyncHTTPClient</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create a new Groq provider.</span>

<span class="sd">    Args:</span>
<span class="sd">        api_key: The API key to use for authentication, if not provided, the `GROQ_API_KEY` environment variable</span>
<span class="sd">            will be used if available.</span>
<span class="sd">        groq_client: An existing</span>
<span class="sd">            [`AsyncGroq`](https://github.com/groq/groq-python?tab=readme-ov-file#async-usage)</span>
<span class="sd">            client to use. If provided, `api_key` and `http_client` must be `None`.</span>
<span class="sd">        http_client: An existing `AsyncHTTPClient` to use for making HTTP requests.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">groq_client</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">assert</span> <span class="n">http_client</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'Cannot provide both `groq_client` and `http_client`'</span>
        <span class="k">assert</span> <span class="n">api_key</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'Cannot provide both `groq_client` and `api_key`'</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">groq_client</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">api_key</span> <span class="o">=</span> <span class="n">api_key</span> <span class="ow">or</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'GROQ_API_KEY'</span><span class="p">)</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">api_key</span><span class="p">:</span>
            <span class="k">raise</span> <span class="n">UserError</span><span class="p">(</span>
                <span class="s1">'Set the `GROQ_API_KEY` environment variable or pass it via `GroqProvider(api_key=...)`'</span>
                <span class="s1">'to use the Groq provider.'</span>
            <span class="p">)</span>
        <span class="k">elif</span> <span class="n">http_client</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">AsyncGroq</span><span class="p">(</span><span class="n">base_url</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">base_url</span><span class="p">,</span> <span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">,</span> <span class="n">http_client</span><span class="o">=</span><span class="n">http_client</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">http_client</span> <span class="o">=</span> <span class="n">cached_async_http_client</span><span class="p">(</span><span class="n">provider</span><span class="o">=</span><span class="s1">'groq'</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">AsyncGroq</span><span class="p">(</span><span class="n">base_url</span><span class="o">=</span><span class="bp">self</span><span class="o">.</span><span class="n">base_url</span><span class="p">,</span> <span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">,</span> <span class="n">http_client</span><span class="o">=</span><span class="n">http_client</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>




  </div>

    </div>

</div>




  </div>

    </div>

</div>

<div class="doc doc-object doc-module">



<a id="pydantic_ai.providers.azure"></a>
    <div class="doc doc-contents first">








  <div class="doc doc-children">



















<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.providers.azure.AzureProvider" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">AzureProvider</span>


</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-internal" title="pydantic_ai.providers.Provider" href="#pydantic_ai.providers.Provider">Provider</a>[<span title="openai.AsyncOpenAI">AsyncOpenAI</span>]</code></p>


        <p>Provider for Azure OpenAI API.</p>
<p>See <a href="https://azure.microsoft.com/en-us/products/ai-foundry">https://azure.microsoft.com/en-us/products/ai-foundry</a> for more information.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/providers/azure.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 22</span>
<span class="normal"> 23</span>
<span class="normal"> 24</span>
<span class="normal"> 25</span>
<span class="normal"> 26</span>
<span class="normal"> 27</span>
<span class="normal"> 28</span>
<span class="normal"> 29</span>
<span class="normal"> 30</span>
<span class="normal"> 31</span>
<span class="normal"> 32</span>
<span class="normal"> 33</span>
<span class="normal"> 34</span>
<span class="normal"> 35</span>
<span class="normal"> 36</span>
<span class="normal"> 37</span>
<span class="normal"> 38</span>
<span class="normal"> 39</span>
<span class="normal"> 40</span>
<span class="normal"> 41</span>
<span class="normal"> 42</span>
<span class="normal"> 43</span>
<span class="normal"> 44</span>
<span class="normal"> 45</span>
<span class="normal"> 46</span>
<span class="normal"> 47</span>
<span class="normal"> 48</span>
<span class="normal"> 49</span>
<span class="normal"> 50</span>
<span class="normal"> 51</span>
<span class="normal"> 52</span>
<span class="normal"> 53</span>
<span class="normal"> 54</span>
<span class="normal"> 55</span>
<span class="normal"> 56</span>
<span class="normal"> 57</span>
<span class="normal"> 58</span>
<span class="normal"> 59</span>
<span class="normal"> 60</span>
<span class="normal"> 61</span>
<span class="normal"> 62</span>
<span class="normal"> 63</span>
<span class="normal"> 64</span>
<span class="normal"> 65</span>
<span class="normal"> 66</span>
<span class="normal"> 67</span>
<span class="normal"> 68</span>
<span class="normal"> 69</span>
<span class="normal"> 70</span>
<span class="normal"> 71</span>
<span class="normal"> 72</span>
<span class="normal"> 73</span>
<span class="normal"> 74</span>
<span class="normal"> 75</span>
<span class="normal"> 76</span>
<span class="normal"> 77</span>
<span class="normal"> 78</span>
<span class="normal"> 79</span>
<span class="normal"> 80</span>
<span class="normal"> 81</span>
<span class="normal"> 82</span>
<span class="normal"> 83</span>
<span class="normal"> 84</span>
<span class="normal"> 85</span>
<span class="normal"> 86</span>
<span class="normal"> 87</span>
<span class="normal"> 88</span>
<span class="normal"> 89</span>
<span class="normal"> 90</span>
<span class="normal"> 91</span>
<span class="normal"> 92</span>
<span class="normal"> 93</span>
<span class="normal"> 94</span>
<span class="normal"> 95</span>
<span class="normal"> 96</span>
<span class="normal"> 97</span>
<span class="normal"> 98</span>
<span class="normal"> 99</span>
<span class="normal">100</span>
<span class="normal">101</span>
<span class="normal">102</span>
<span class="normal">103</span>
<span class="normal">104</span>
<span class="normal">105</span>
<span class="normal">106</span>
<span class="normal">107</span></pre></div></td><td class="code"><div><pre id="__code_23"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_23 > code"></button><code tabindex="0"><span class="k">class</span><span class="w"> </span><span class="nc">AzureProvider</span><span class="p">(</span><span class="n">Provider</span><span class="p">[</span><span class="n">AsyncOpenAI</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""Provider for Azure OpenAI API.</span>

<span class="sd">    See &lt;https://azure.microsoft.com/en-us/products/ai-foundry&gt; for more information.</span>
<span class="sd">    """</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s1">'azure'</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">base_url</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">assert</span> <span class="bp">self</span><span class="o">.</span><span class="n">_base_url</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_base_url</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncOpenAI</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span>

    <span class="nd">@overload</span>
    <span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">openai_client</span><span class="p">:</span> <span class="n">AsyncAzureOpenAI</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span> <span class="o">...</span>

    <span class="nd">@overload</span>
    <span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">azure_endpoint</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">api_version</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">http_client</span><span class="p">:</span> <span class="n">httpx</span><span class="o">.</span><span class="n">AsyncClient</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span> <span class="o">...</span>

    <span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">azure_endpoint</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">api_version</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">openai_client</span><span class="p">:</span> <span class="n">AsyncAzureOpenAI</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">http_client</span><span class="p">:</span> <span class="n">httpx</span><span class="o">.</span><span class="n">AsyncClient</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create a new Azure provider.</span>

<span class="sd">        Args:</span>
<span class="sd">            azure_endpoint: The Azure endpoint to use for authentication, if not provided, the `AZURE_OPENAI_ENDPOINT`</span>
<span class="sd">                environment variable will be used if available.</span>
<span class="sd">            api_version: The API version to use for authentication, if not provided, the `OPENAI_API_VERSION`</span>
<span class="sd">                environment variable will be used if available.</span>
<span class="sd">            api_key: The API key to use for authentication, if not provided, the `AZURE_OPENAI_API_KEY` environment variable</span>
<span class="sd">                will be used if available.</span>
<span class="sd">            openai_client: An existing</span>
<span class="sd">                [`AsyncAzureOpenAI`](https://github.com/openai/openai-python#microsoft-azure-openai)</span>
<span class="sd">                client to use. If provided, `base_url`, `api_key`, and `http_client` must be `None`.</span>
<span class="sd">            http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">openai_client</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">assert</span> <span class="n">azure_endpoint</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'Cannot provide both `openai_client` and `azure_endpoint`'</span>
            <span class="k">assert</span> <span class="n">http_client</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'Cannot provide both `openai_client` and `http_client`'</span>
            <span class="k">assert</span> <span class="n">api_key</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'Cannot provide both `openai_client` and `api_key`'</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_base_url</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">openai_client</span><span class="o">.</span><span class="n">base_url</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">openai_client</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">azure_endpoint</span> <span class="o">=</span> <span class="n">azure_endpoint</span> <span class="ow">or</span> <span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="s1">'AZURE_OPENAI_ENDPOINT'</span><span class="p">)</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">azure_endpoint</span><span class="p">:</span>  <span class="c1"># pragma: no cover</span>
                <span class="k">raise</span> <span class="n">UserError</span><span class="p">(</span>
                    <span class="s1">'Must provide one of the `azure_endpoint` argument or the `AZURE_OPENAI_ENDPOINT` environment variable'</span>
                <span class="p">)</span>

            <span class="k">if</span> <span class="ow">not</span> <span class="n">api_key</span> <span class="ow">and</span> <span class="s1">'OPENAI_API_KEY'</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="p">:</span>  <span class="c1"># pragma: no cover</span>
                <span class="k">raise</span> <span class="n">UserError</span><span class="p">(</span>
                    <span class="s1">'Must provide one of the `api_key` argument or the `OPENAI_API_KEY` environment variable'</span>
                <span class="p">)</span>

            <span class="k">if</span> <span class="ow">not</span> <span class="n">api_version</span> <span class="ow">and</span> <span class="s1">'OPENAI_API_VERSION'</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="p">:</span>  <span class="c1"># pragma: no cover</span>
                <span class="k">raise</span> <span class="n">UserError</span><span class="p">(</span>
                    <span class="s1">'Must provide one of the `api_version` argument or the `OPENAI_API_VERSION` environment variable'</span>
                <span class="p">)</span>

            <span class="n">http_client</span> <span class="o">=</span> <span class="n">http_client</span> <span class="ow">or</span> <span class="n">cached_async_http_client</span><span class="p">(</span><span class="n">provider</span><span class="o">=</span><span class="s1">'azure'</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">AsyncAzureOpenAI</span><span class="p">(</span>
                <span class="n">azure_endpoint</span><span class="o">=</span><span class="n">azure_endpoint</span><span class="p">,</span>
                <span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">,</span>
                <span class="n">api_version</span><span class="o">=</span><span class="n">api_version</span><span class="p">,</span>
                <span class="n">http_client</span><span class="o">=</span><span class="n">http_client</span><span class="p">,</span>
            <span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_base_url</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">base_url</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.providers.azure.AzureProvider.__init__" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">__init__</span>


</h4>
          <div class="doc-overloads">
<div class="language-python doc-signature highlight"><pre id="__code_24"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_24 > code"></button><code><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="p">,</span> <span class="nf">openai_client</span><span class="p">:</span> <span class="n"><span title="openai.AsyncAzureOpenAI">AsyncAzureOpenAI</span></span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span>
</code></pre></div><div class="language-python doc-signature highlight"><pre id="__code_25"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_25 > code"></button><code><span class="fm">__init__</span><span class="p">(</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="nf">azure_endpoint</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">api_version</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">api_key</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">http_client</span><span class="p">:</span> <span class="n"><span title="httpx.AsyncClient">AsyncClient</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span>
</code></pre></div>          </div>
<div class="language-python doc-signature highlight"><pre id="__code_26"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_26 > code"></button><code><span class="fm">__init__</span><span class="p">(</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="nf">azure_endpoint</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">api_version</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">api_key</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">openai_client</span><span class="p">:</span> <span class="n"><span title="openai.AsyncAzureOpenAI">AsyncAzureOpenAI</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">http_client</span><span class="p">:</span> <span class="n"><span title="httpx.AsyncClient">AsyncClient</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Create a new Azure provider.</p>


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
                <code>azure_endpoint</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The Azure endpoint to use for authentication, if not provided, the <code>AZURE_OPENAI_ENDPOINT</code>
environment variable will be used if available.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>api_version</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The API version to use for authentication, if not provided, the <code>OPENAI_API_VERSION</code>
environment variable will be used if available.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>api_key</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The API key to use for authentication, if not provided, the <code>AZURE_OPENAI_API_KEY</code> environment variable
will be used if available.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>openai_client</code>
            </td>
            <td>
                  <code><span title="openai.AsyncAzureOpenAI">AsyncAzureOpenAI</span> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>An existing
<a href="https://github.com/openai/openai-python#microsoft-azure-openai"><code>AsyncAzureOpenAI</code></a>
client to use. If provided, <code>base_url</code>, <code>api_key</code>, and <code>http_client</code> must be <code>None</code>.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>http_client</code>
            </td>
            <td>
                  <code><span title="httpx.AsyncClient">AsyncClient</span> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>An existing <code>httpx.AsyncClient</code> to use for making HTTP requests.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/providers/azure.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal"> 54</span>
<span class="normal"> 55</span>
<span class="normal"> 56</span>
<span class="normal"> 57</span>
<span class="normal"> 58</span>
<span class="normal"> 59</span>
<span class="normal"> 60</span>
<span class="normal"> 61</span>
<span class="normal"> 62</span>
<span class="normal"> 63</span>
<span class="normal"> 64</span>
<span class="normal"> 65</span>
<span class="normal"> 66</span>
<span class="normal"> 67</span>
<span class="normal"> 68</span>
<span class="normal"> 69</span>
<span class="normal"> 70</span>
<span class="normal"> 71</span>
<span class="normal"> 72</span>
<span class="normal"> 73</span>
<span class="normal"> 74</span>
<span class="normal"> 75</span>
<span class="normal"> 76</span>
<span class="normal"> 77</span>
<span class="normal"> 78</span>
<span class="normal"> 79</span>
<span class="normal"> 80</span>
<span class="normal"> 81</span>
<span class="normal"> 82</span>
<span class="normal"> 83</span>
<span class="normal"> 84</span>
<span class="normal"> 85</span>
<span class="normal"> 86</span>
<span class="normal"> 87</span>
<span class="normal"> 88</span>
<span class="normal"> 89</span>
<span class="normal"> 90</span>
<span class="normal"> 91</span>
<span class="normal"> 92</span>
<span class="normal"> 93</span>
<span class="normal"> 94</span>
<span class="normal"> 95</span>
<span class="normal"> 96</span>
<span class="normal"> 97</span>
<span class="normal"> 98</span>
<span class="normal"> 99</span>
<span class="normal">100</span>
<span class="normal">101</span>
<span class="normal">102</span>
<span class="normal">103</span>
<span class="normal">104</span>
<span class="normal">105</span>
<span class="normal">106</span>
<span class="normal">107</span></pre></div></td><td class="code"><div><pre id="__code_27"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_27 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">azure_endpoint</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">api_version</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">openai_client</span><span class="p">:</span> <span class="n">AsyncAzureOpenAI</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">http_client</span><span class="p">:</span> <span class="n">httpx</span><span class="o">.</span><span class="n">AsyncClient</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create a new Azure provider.</span>

<span class="sd">    Args:</span>
<span class="sd">        azure_endpoint: The Azure endpoint to use for authentication, if not provided, the `AZURE_OPENAI_ENDPOINT`</span>
<span class="sd">            environment variable will be used if available.</span>
<span class="sd">        api_version: The API version to use for authentication, if not provided, the `OPENAI_API_VERSION`</span>
<span class="sd">            environment variable will be used if available.</span>
<span class="sd">        api_key: The API key to use for authentication, if not provided, the `AZURE_OPENAI_API_KEY` environment variable</span>
<span class="sd">            will be used if available.</span>
<span class="sd">        openai_client: An existing</span>
<span class="sd">            [`AsyncAzureOpenAI`](https://github.com/openai/openai-python#microsoft-azure-openai)</span>
<span class="sd">            client to use. If provided, `base_url`, `api_key`, and `http_client` must be `None`.</span>
<span class="sd">        http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">openai_client</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">assert</span> <span class="n">azure_endpoint</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'Cannot provide both `openai_client` and `azure_endpoint`'</span>
        <span class="k">assert</span> <span class="n">http_client</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'Cannot provide both `openai_client` and `http_client`'</span>
        <span class="k">assert</span> <span class="n">api_key</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'Cannot provide both `openai_client` and `api_key`'</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_base_url</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="n">openai_client</span><span class="o">.</span><span class="n">base_url</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">openai_client</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">azure_endpoint</span> <span class="o">=</span> <span class="n">azure_endpoint</span> <span class="ow">or</span> <span class="n">os</span><span class="o">.</span><span class="n">getenv</span><span class="p">(</span><span class="s1">'AZURE_OPENAI_ENDPOINT'</span><span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">azure_endpoint</span><span class="p">:</span>  <span class="c1"># pragma: no cover</span>
            <span class="k">raise</span> <span class="n">UserError</span><span class="p">(</span>
                <span class="s1">'Must provide one of the `azure_endpoint` argument or the `AZURE_OPENAI_ENDPOINT` environment variable'</span>
            <span class="p">)</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">api_key</span> <span class="ow">and</span> <span class="s1">'OPENAI_API_KEY'</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="p">:</span>  <span class="c1"># pragma: no cover</span>
            <span class="k">raise</span> <span class="n">UserError</span><span class="p">(</span>
                <span class="s1">'Must provide one of the `api_key` argument or the `OPENAI_API_KEY` environment variable'</span>
            <span class="p">)</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">api_version</span> <span class="ow">and</span> <span class="s1">'OPENAI_API_VERSION'</span> <span class="ow">not</span> <span class="ow">in</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="p">:</span>  <span class="c1"># pragma: no cover</span>
            <span class="k">raise</span> <span class="n">UserError</span><span class="p">(</span>
                <span class="s1">'Must provide one of the `api_version` argument or the `OPENAI_API_VERSION` environment variable'</span>
            <span class="p">)</span>

        <span class="n">http_client</span> <span class="o">=</span> <span class="n">http_client</span> <span class="ow">or</span> <span class="n">cached_async_http_client</span><span class="p">(</span><span class="n">provider</span><span class="o">=</span><span class="s1">'azure'</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">AsyncAzureOpenAI</span><span class="p">(</span>
            <span class="n">azure_endpoint</span><span class="o">=</span><span class="n">azure_endpoint</span><span class="p">,</span>
            <span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">,</span>
            <span class="n">api_version</span><span class="o">=</span><span class="n">api_version</span><span class="p">,</span>
            <span class="n">http_client</span><span class="o">=</span><span class="n">http_client</span><span class="p">,</span>
        <span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_base_url</span> <span class="o">=</span> <span class="nb">str</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">_client</span><span class="o">.</span><span class="n">base_url</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>




  </div>

    </div>

</div>




  </div>

    </div>

</div>

<div class="doc doc-object doc-module">



<a id="pydantic_ai.providers.cohere"></a>
    <div class="doc doc-contents first">








  <div class="doc doc-children">



















<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.providers.cohere.CohereProvider" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">CohereProvider</span>


</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-internal" title="pydantic_ai.providers.Provider" href="#pydantic_ai.providers.Provider">Provider</a>[<span title="cohere.AsyncClientV2">AsyncClientV2</span>]</code></p>


        <p>Provider for Cohere API.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/providers/cohere.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">20</span>
<span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span></pre></div></td><td class="code"><div><pre id="__code_28"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_28 > code"></button><code tabindex="0"><span class="k">class</span><span class="w"> </span><span class="nc">CohereProvider</span><span class="p">(</span><span class="n">Provider</span><span class="p">[</span><span class="n">AsyncClientV2</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""Provider for Cohere API."""</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s1">'cohere'</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">base_url</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="n">client_wrapper</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">_client_wrapper</span>  <span class="c1"># type: ignore</span>
        <span class="k">return</span> <span class="nb">str</span><span class="p">(</span><span class="n">client_wrapper</span><span class="o">.</span><span class="n">get_base_url</span><span class="p">())</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncClientV2</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span>

    <span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">cohere_client</span><span class="p">:</span> <span class="n">AsyncClientV2</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">http_client</span><span class="p">:</span> <span class="n">AsyncHTTPClient</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create a new Cohere provider.</span>

<span class="sd">        Args:</span>
<span class="sd">            api_key: The API key to use for authentication, if not provided, the `CO_API_KEY` environment variable</span>
<span class="sd">                will be used if available.</span>
<span class="sd">            cohere_client: An existing</span>
<span class="sd">                [AsyncClientV2](https://github.com/cohere-ai/cohere-python)</span>
<span class="sd">                client to use. If provided, `api_key` and `http_client` must be `None`.</span>
<span class="sd">            http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">cohere_client</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">assert</span> <span class="n">http_client</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'Cannot provide both `cohere_client` and `http_client`'</span>
            <span class="k">assert</span> <span class="n">api_key</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'Cannot provide both `cohere_client` and `api_key`'</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">cohere_client</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">api_key</span> <span class="o">=</span> <span class="n">api_key</span> <span class="ow">or</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'CO_API_KEY'</span><span class="p">)</span>
            <span class="k">if</span> <span class="ow">not</span> <span class="n">api_key</span><span class="p">:</span>
                <span class="k">raise</span> <span class="n">UserError</span><span class="p">(</span>
                    <span class="s1">'Set the `CO_API_KEY` environment variable or pass it via `CohereProvider(api_key=...)`'</span>
                    <span class="s1">'to use the Cohere provider.'</span>
                <span class="p">)</span>

            <span class="n">base_url</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'CO_BASE_URL'</span><span class="p">)</span>
            <span class="k">if</span> <span class="n">http_client</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">AsyncClientV2</span><span class="p">(</span><span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">,</span> <span class="n">httpx_client</span><span class="o">=</span><span class="n">http_client</span><span class="p">,</span> <span class="n">base_url</span><span class="o">=</span><span class="n">base_url</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">http_client</span> <span class="o">=</span> <span class="n">cached_async_http_client</span><span class="p">(</span><span class="n">provider</span><span class="o">=</span><span class="s1">'cohere'</span><span class="p">)</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">AsyncClientV2</span><span class="p">(</span><span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">,</span> <span class="n">httpx_client</span><span class="o">=</span><span class="n">http_client</span><span class="p">,</span> <span class="n">base_url</span><span class="o">=</span><span class="n">base_url</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.providers.cohere.CohereProvider.__init__" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">__init__</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_29"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_29 > code"></button><code><span class="fm">__init__</span><span class="p">(</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="nf">api_key</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">cohere_client</span><span class="p">:</span> <span class="n"><span title="cohere.AsyncClientV2">AsyncClientV2</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">http_client</span><span class="p">:</span> <span class="n"><span title="httpx.AsyncClient">AsyncClient</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Create a new Cohere provider.</p>


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
                <code>api_key</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The API key to use for authentication, if not provided, the <code>CO_API_KEY</code> environment variable
will be used if available.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>cohere_client</code>
            </td>
            <td>
                  <code><span title="cohere.AsyncClientV2">AsyncClientV2</span> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>An existing
<a href="https://github.com/cohere-ai/cohere-python">AsyncClientV2</a>
client to use. If provided, <code>api_key</code> and <code>http_client</code> must be <code>None</code>.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>http_client</code>
            </td>
            <td>
                  <code><span title="httpx.AsyncClient">AsyncClient</span> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>An existing <code>httpx.AsyncClient</code> to use for making HTTP requests.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/providers/cohere.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span></pre></div></td><td class="code"><div><pre id="__code_30"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_30 > code"></button><code><span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">cohere_client</span><span class="p">:</span> <span class="n">AsyncClientV2</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">http_client</span><span class="p">:</span> <span class="n">AsyncHTTPClient</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create a new Cohere provider.</span>

<span class="sd">    Args:</span>
<span class="sd">        api_key: The API key to use for authentication, if not provided, the `CO_API_KEY` environment variable</span>
<span class="sd">            will be used if available.</span>
<span class="sd">        cohere_client: An existing</span>
<span class="sd">            [AsyncClientV2](https://github.com/cohere-ai/cohere-python)</span>
<span class="sd">            client to use. If provided, `api_key` and `http_client` must be `None`.</span>
<span class="sd">        http_client: An existing `httpx.AsyncClient` to use for making HTTP requests.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">cohere_client</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">assert</span> <span class="n">http_client</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'Cannot provide both `cohere_client` and `http_client`'</span>
        <span class="k">assert</span> <span class="n">api_key</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'Cannot provide both `cohere_client` and `api_key`'</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">cohere_client</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">api_key</span> <span class="o">=</span> <span class="n">api_key</span> <span class="ow">or</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'CO_API_KEY'</span><span class="p">)</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">api_key</span><span class="p">:</span>
            <span class="k">raise</span> <span class="n">UserError</span><span class="p">(</span>
                <span class="s1">'Set the `CO_API_KEY` environment variable or pass it via `CohereProvider(api_key=...)`'</span>
                <span class="s1">'to use the Cohere provider.'</span>
            <span class="p">)</span>

        <span class="n">base_url</span> <span class="o">=</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'CO_BASE_URL'</span><span class="p">)</span>
        <span class="k">if</span> <span class="n">http_client</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">AsyncClientV2</span><span class="p">(</span><span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">,</span> <span class="n">httpx_client</span><span class="o">=</span><span class="n">http_client</span><span class="p">,</span> <span class="n">base_url</span><span class="o">=</span><span class="n">base_url</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">http_client</span> <span class="o">=</span> <span class="n">cached_async_http_client</span><span class="p">(</span><span class="n">provider</span><span class="o">=</span><span class="s1">'cohere'</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">AsyncClientV2</span><span class="p">(</span><span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">,</span> <span class="n">httpx_client</span><span class="o">=</span><span class="n">http_client</span><span class="p">,</span> <span class="n">base_url</span><span class="o">=</span><span class="n">base_url</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>




  </div>

    </div>

</div>




  </div>

    </div>

</div>

<div class="doc doc-object doc-module">



<a id="pydantic_ai.providers.mistral"></a>
    <div class="doc doc-contents first">








  <div class="doc doc-children">



















<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.providers.mistral.MistralProvider" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">MistralProvider</span>


</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-internal" title="pydantic_ai.providers.Provider" href="#pydantic_ai.providers.Provider">Provider</a>[<span title="mistralai.Mistral">Mistral</span>]</code></p>


        <p>Provider for Mistral API.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/providers/mistral.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">21</span>
<span class="normal">22</span>
<span class="normal">23</span>
<span class="normal">24</span>
<span class="normal">25</span>
<span class="normal">26</span>
<span class="normal">27</span>
<span class="normal">28</span>
<span class="normal">29</span>
<span class="normal">30</span>
<span class="normal">31</span>
<span class="normal">32</span>
<span class="normal">33</span>
<span class="normal">34</span>
<span class="normal">35</span>
<span class="normal">36</span>
<span class="normal">37</span>
<span class="normal">38</span>
<span class="normal">39</span>
<span class="normal">40</span>
<span class="normal">41</span>
<span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span></pre></div></td><td class="code"><div><pre id="__code_31"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_31 > code"></button><code tabindex="0"><span class="k">class</span><span class="w"> </span><span class="nc">MistralProvider</span><span class="p">(</span><span class="n">Provider</span><span class="p">[</span><span class="n">Mistral</span><span class="p">]):</span>
<span class="w">    </span><span class="sd">"""Provider for Mistral API."""</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">name</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="s1">'mistral'</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">base_url</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">client</span><span class="o">.</span><span class="n">sdk_configuration</span><span class="o">.</span><span class="n">get_server_details</span><span class="p">()[</span><span class="mi">0</span><span class="p">]</span>

    <span class="nd">@property</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">client</span><span class="p">(</span><span class="bp">self</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Mistral</span><span class="p">:</span>
        <span class="k">return</span> <span class="bp">self</span><span class="o">.</span><span class="n">_client</span>

    <span class="nd">@overload</span>
    <span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">mistral_client</span><span class="p">:</span> <span class="n">Mistral</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span> <span class="o">...</span>

    <span class="nd">@overload</span>
    <span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="o">*</span><span class="p">,</span> <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span> <span class="n">http_client</span><span class="p">:</span> <span class="n">AsyncHTTPClient</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span> <span class="o">...</span>

    <span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">mistral_client</span><span class="p">:</span> <span class="n">Mistral</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">http_client</span><span class="p">:</span> <span class="n">AsyncHTTPClient</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">        </span><span class="sd">"""Create a new Mistral provider.</span>

<span class="sd">        Args:</span>
<span class="sd">            api_key: The API key to use for authentication, if not provided, the `MISTRAL_API_KEY` environment variable</span>
<span class="sd">                will be used if available.</span>
<span class="sd">            mistral_client: An existing `Mistral` client to use, if provided, `api_key` and `http_client` must be `None`.</span>
<span class="sd">            http_client: An existing async client to use for making HTTP requests.</span>
<span class="sd">        """</span>
        <span class="k">if</span> <span class="n">mistral_client</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="k">assert</span> <span class="n">http_client</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'Cannot provide both `mistral_client` and `http_client`'</span>
            <span class="k">assert</span> <span class="n">api_key</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'Cannot provide both `mistral_client` and `api_key`'</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">mistral_client</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">api_key</span> <span class="o">=</span> <span class="n">api_key</span> <span class="ow">or</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'MISTRAL_API_KEY'</span><span class="p">)</span>

            <span class="k">if</span> <span class="ow">not</span> <span class="n">api_key</span><span class="p">:</span>
                <span class="k">raise</span> <span class="n">UserError</span><span class="p">(</span>
                    <span class="s1">'Set the `MISTRAL_API_KEY` environment variable or pass it via `MistralProvider(api_key=...)`'</span>
                    <span class="s1">'to use the Mistral provider.'</span>
                <span class="p">)</span>
            <span class="k">elif</span> <span class="n">http_client</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">Mistral</span><span class="p">(</span><span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">,</span> <span class="n">async_client</span><span class="o">=</span><span class="n">http_client</span><span class="p">)</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="n">http_client</span> <span class="o">=</span> <span class="n">cached_async_http_client</span><span class="p">(</span><span class="n">provider</span><span class="o">=</span><span class="s1">'mistral'</span><span class="p">)</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">Mistral</span><span class="p">(</span><span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">,</span> <span class="n">async_client</span><span class="o">=</span><span class="n">http_client</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.providers.mistral.MistralProvider.__init__" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">__init__</span>


</h4>
          <div class="doc-overloads">
<div class="language-python doc-signature highlight"><pre id="__code_32"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_32 > code"></button><code><span class="fm">__init__</span><span class="p">(</span><span class="o">*</span><span class="p">,</span> <span class="nf">mistral_client</span><span class="p">:</span> <span class="n"><span title="mistralai.Mistral">Mistral</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span>
</code></pre></div><div class="language-python doc-signature highlight"><pre id="__code_33"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_33 > code"></button><code><span class="fm">__init__</span><span class="p">(</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="nf">api_key</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">http_client</span><span class="p">:</span> <span class="n"><span title="httpx.AsyncClient">AsyncClient</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span>
</code></pre></div>          </div>
<div class="language-python doc-signature highlight"><pre id="__code_34"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_34 > code"></button><code><span class="fm">__init__</span><span class="p">(</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="nf">api_key</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">mistral_client</span><span class="p">:</span> <span class="n"><span title="mistralai.Mistral">Mistral</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">http_client</span><span class="p">:</span> <span class="n"><span title="httpx.AsyncClient">AsyncClient</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Create a new Mistral provider.</p>


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
                <code>api_key</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" href="https://docs.python.org/3/library/stdtypes.html#str">str</a> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The API key to use for authentication, if not provided, the <code>MISTRAL_API_KEY</code> environment variable
will be used if available.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>mistral_client</code>
            </td>
            <td>
                  <code><span title="mistralai.Mistral">Mistral</span> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>An existing <code>Mistral</code> client to use, if provided, <code>api_key</code> and <code>http_client</code> must be <code>None</code>.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>http_client</code>
            </td>
            <td>
                  <code><span title="httpx.AsyncClient">AsyncClient</span> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>An existing async client to use for making HTTP requests.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/providers/mistral.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">42</span>
<span class="normal">43</span>
<span class="normal">44</span>
<span class="normal">45</span>
<span class="normal">46</span>
<span class="normal">47</span>
<span class="normal">48</span>
<span class="normal">49</span>
<span class="normal">50</span>
<span class="normal">51</span>
<span class="normal">52</span>
<span class="normal">53</span>
<span class="normal">54</span>
<span class="normal">55</span>
<span class="normal">56</span>
<span class="normal">57</span>
<span class="normal">58</span>
<span class="normal">59</span>
<span class="normal">60</span>
<span class="normal">61</span>
<span class="normal">62</span>
<span class="normal">63</span>
<span class="normal">64</span>
<span class="normal">65</span>
<span class="normal">66</span>
<span class="normal">67</span>
<span class="normal">68</span>
<span class="normal">69</span>
<span class="normal">70</span>
<span class="normal">71</span>
<span class="normal">72</span>
<span class="normal">73</span></pre></div></td><td class="code"><div><pre id="__code_35"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_35 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">api_key</span><span class="p">:</span> <span class="nb">str</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">mistral_client</span><span class="p">:</span> <span class="n">Mistral</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">http_client</span><span class="p">:</span> <span class="n">AsyncHTTPClient</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Create a new Mistral provider.</span>

<span class="sd">    Args:</span>
<span class="sd">        api_key: The API key to use for authentication, if not provided, the `MISTRAL_API_KEY` environment variable</span>
<span class="sd">            will be used if available.</span>
<span class="sd">        mistral_client: An existing `Mistral` client to use, if provided, `api_key` and `http_client` must be `None`.</span>
<span class="sd">        http_client: An existing async client to use for making HTTP requests.</span>
<span class="sd">    """</span>
    <span class="k">if</span> <span class="n">mistral_client</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">assert</span> <span class="n">http_client</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'Cannot provide both `mistral_client` and `http_client`'</span>
        <span class="k">assert</span> <span class="n">api_key</span> <span class="ow">is</span> <span class="kc">None</span><span class="p">,</span> <span class="s1">'Cannot provide both `mistral_client` and `api_key`'</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">mistral_client</span>
    <span class="k">else</span><span class="p">:</span>
        <span class="n">api_key</span> <span class="o">=</span> <span class="n">api_key</span> <span class="ow">or</span> <span class="n">os</span><span class="o">.</span><span class="n">environ</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="s1">'MISTRAL_API_KEY'</span><span class="p">)</span>

        <span class="k">if</span> <span class="ow">not</span> <span class="n">api_key</span><span class="p">:</span>
            <span class="k">raise</span> <span class="n">UserError</span><span class="p">(</span>
                <span class="s1">'Set the `MISTRAL_API_KEY` environment variable or pass it via `MistralProvider(api_key=...)`'</span>
                <span class="s1">'to use the Mistral provider.'</span>
            <span class="p">)</span>
        <span class="k">elif</span> <span class="n">http_client</span> <span class="ow">is</span> <span class="ow">not</span> <span class="kc">None</span><span class="p">:</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">Mistral</span><span class="p">(</span><span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">,</span> <span class="n">async_client</span><span class="o">=</span><span class="n">http_client</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">http_client</span> <span class="o">=</span> <span class="n">cached_async_http_client</span><span class="p">(</span><span class="n">provider</span><span class="o">=</span><span class="s1">'mistral'</span><span class="p">)</span>
            <span class="bp">self</span><span class="o">.</span><span class="n">_client</span> <span class="o">=</span> <span class="n">Mistral</span><span class="p">(</span><span class="n">api_key</span><span class="o">=</span><span class="n">api_key</span><span class="p">,</span> <span class="n">async_client</span><span class="o">=</span><span class="n">http_client</span><span class="p">)</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>




  </div>

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
    
    
    <script id="__config" type="application/json">{"base": "../..", "features": ["search.suggest", "search.highlight", "content.tabs.link", "content.code.annotate", "content.code.copy", "content.code.select", "navigation.path", "navigation.indexes", "navigation.sections", "navigation.tracking", "toc.follow"], "search": "../../assets/javascripts/workers/search.f8cc74c7.min.js", "translations": {"clipboard.copied": "Copied to clipboard", "clipboard.copy": "Copy to clipboard", "search.result.more.one": "1 more on this page", "search.result.more.other": "# more on this page", "search.result.none": "No matching documents", "search.result.one": "1 matching document", "search.result.other": "# matching documents", "search.result.placeholder": "Type to start searching", "search.result.term.missing": "Missing", "select.version": "Select version"}}</script>
    
    
      <script src="../../assets/javascripts/bundle.f1b6f286.min.js"></script>
      
        <script src="/flarelytics/client.js"></script>
      
        <script src="https://cdn.jsdelivr.net/npm/algoliasearch@5.20.0/dist/lite/builds/browser.umd.js"></script>
      
        <script src="https://cdn.jsdelivr.net/npm/instantsearch.js@4.77.3/dist/instantsearch.production.min.js"></script>
      
        <script src="/javascripts/algolia-search.js"></script>
      
    
  <script id="init-glightbox">const lightbox = GLightbox({"touchNavigation": true, "loop": false, "zoomable": true, "draggable": true, "openEffect": "zoom", "closeEffect": "zoom", "slideEffect": "slide"});
document$.subscribe(() => { lightbox.reload() });
</script>
</body></html>