<!DOCTYPE html><html lang="en" class="js-focus-visible js" data-js-focus-visible=""><head>
    
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width,initial-scale=1">
      
        <meta name="description" content="Agent Framework / shim to use Pydantic with LLMs">
      
      
      
        <link rel="canonical" href="https://ai.pydantic.dev/api/models/instrumented/">
      
      
        <link rel="prev" href="../groq/">
      
      
        <link rel="next" href="../mistral/">
      
      
      <link rel="icon" href="../../../favicon.ico">
      <meta name="generator" content="mkdocs-1.6.1, mkdocs-material-9.6.5">
    
    
      
        <title>pydantic_ai.models.instrumented - PydanticAI</title>
      
    
    
      <link rel="stylesheet" href="../../../assets/stylesheets/main.8608ea7d.min.css">
      
        
        <link rel="stylesheet" href="../../../assets/stylesheets/palette.06af60db.min.css">
      
      


    
    
      
    
    
      
        
        
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin="">
        <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:300,300i,400,400i,700,700i%7CRoboto+Mono:400,400i,700,700i&amp;display=fallback">
        <style>:root{--md-text-font:"Roboto";--md-code-font:"Roboto Mono"}</style>
      
    
    
      <link rel="stylesheet" href="../../../assets/_mkdocstrings.css">
    
      <link rel="stylesheet" href="../../../extra/tweaks.css">
    
    <script>__md_scope=new URL("../../..",location),__md_hash=e=>[...e].reduce(((e,_)=>(e<<5)-e+_.charCodeAt(0)),0),__md_get=(e,_=localStorage,t=__md_scope)=>JSON.parse(_.getItem(t.pathname+"."+e)),__md_set=(e,_,t=localStorage,a=__md_scope)=>{try{t.setItem(a.pathname+"."+e,JSON.stringify(_))}catch(e){}}</script>
    
      

    
    
      
        <meta property="og:type" content="website">
      
        <meta property="og:title" content="pydantic_ai.models.instrumented - PydanticAI">
      
        <meta property="og:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta property="og:image" content="https://ai.pydantic.dev/assets/images/social/api/models/instrumented.png">
      
        <meta property="og:image:type" content="image/png">
      
        <meta property="og:image:width" content="1200">
      
        <meta property="og:image:height" content="630">
      
        <meta property="og:url" content="https://ai.pydantic.dev/api/models/instrumented/">
      
        <meta name="twitter:card" content="summary_large_image">
      
        <meta name="twitter:title" content="pydantic_ai.models.instrumented - PydanticAI">
      
        <meta name="twitter:description" content="Agent Framework / shim to use Pydantic with LLMs">
      
        <meta name="twitter:image" content="https://ai.pydantic.dev/assets/images/social/api/models/instrumented.png">
      
    
    
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
      
        
        <a href="#pydantic_aimodelsinstrumented" class="md-skip">
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
            
              pydantic_ai.models.instrumented
            
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
  

              
            
              
                
  
  
  
  
    <li class="md-nav__item">
      <a href="../base/" class="md-nav__link">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models
    
  </span>
  

      </a>
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
  

              
            
              
                
  
  
    
  
  
  
    <li class="md-nav__item md-nav__item--active">
      
      <input class="md-nav__toggle md-toggle" type="checkbox" id="__toc">
      
      
        
      
      
        <label class="md-nav__link md-nav__link--active" for="__toc">
          
  
  <span class="md-ellipsis">
    pydantic_ai.models.instrumented
    
  </span>
  

          <span class="md-nav__icon md-icon"></span>
        </label>
      
      <a href="./" class="md-nav__link md-nav__link--active">
        
  
  <span class="md-ellipsis">
    pydantic_ai.models.instrumented
    
  </span>
  

      </a>
      
        

<nav class="md-nav md-nav--secondary" aria-label="Table of contents">
  
  
  
    
  
  
    <label class="md-nav__title" for="__toc">
      <span class="md-nav__icon md-icon"></span>
      Table of contents
    </label>
    <ul class="md-nav__list" data-md-component="toc">
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.models.instrumented" class="md-nav__link">
    <span class="md-ellipsis">
      instrumented
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.models.instrumented.InstrumentationSettings" class="md-nav__link">
    <span class="md-ellipsis">
      InstrumentationSettings
    </span>
  </a>
  
    <nav class="md-nav" aria-label="InstrumentationSettings">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.instrumented.InstrumentationSettings.__init__" class="md-nav__link">
    <span class="md-ellipsis">
      __init__
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.models.instrumented.InstrumentedModel" class="md-nav__link">
    <span class="md-ellipsis">
      InstrumentedModel
    </span>
  </a>
  
    <nav class="md-nav" aria-label="InstrumentedModel">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.instrumented.InstrumentedModel.settings" class="md-nav__link">
    <span class="md-ellipsis">
      settings
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
  <a href="#pydantic_ai.models.instrumented" class="md-nav__link">
    <span class="md-ellipsis">
      instrumented
    </span>
  </a>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.models.instrumented.InstrumentationSettings" class="md-nav__link">
    <span class="md-ellipsis">
      InstrumentationSettings
    </span>
  </a>
  
    <nav class="md-nav" aria-label="InstrumentationSettings">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.instrumented.InstrumentationSettings.__init__" class="md-nav__link">
    <span class="md-ellipsis">
      __init__
    </span>
  </a>
  
</li>
        
      </ul>
    </nav>
  
</li>
      
        <li class="md-nav__item">
  <a href="#pydantic_ai.models.instrumented.InstrumentedModel" class="md-nav__link">
    <span class="md-ellipsis">
      InstrumentedModel
    </span>
  </a>
  
    <nav class="md-nav" aria-label="InstrumentedModel">
      <ul class="md-nav__list">
        
          <li class="md-nav__item">
  <a href="#pydantic_ai.models.instrumented.InstrumentedModel.settings" class="md-nav__link">
    <span class="md-ellipsis">
      settings
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
                
                  


  
  


<h1 id="pydantic_aimodelsinstrumented">pydantic_ai.models.instrumented</h1>


<div class="doc doc-object doc-module">



<a id="pydantic_ai.models.instrumented"></a>
    <div class="doc doc-contents first">








  <div class="doc doc-children">















































<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.models.instrumented.InstrumentationSettings" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">InstrumentationSettings</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">


        <p>Options for instrumenting models and agents with OpenTelemetry.</p>
<p>Used in:</p>
<ul>
<li><code>Agent(instrument=...)</code></li>
<li><a class="autorefs autorefs-internal" href="../../agent/#pydantic_ai.agent.Agent.instrument_all"><code>Agent.instrument_all()</code></a></li>
<li><a class="autorefs autorefs-internal" href="#pydantic_ai.models.instrumented.InstrumentedModel"><code>InstrumentedModel</code></a></li>
</ul>
<p>See the <a href="https://ai.pydantic.dev/logfire/">Debugging and Monitoring guide</a> for more info.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/models/instrumented.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">52</span>
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
<span class="normal">88</span>
<span class="normal">89</span>
<span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span>
<span class="normal">94</span>
<span class="normal">95</span></pre></div></td><td class="code"><div><pre id="__code_0"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_0 > code"></button><code tabindex="0"><span class="nd">@dataclass</span><span class="p">(</span><span class="n">init</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
<span class="k">class</span><span class="w"> </span><span class="nc">InstrumentationSettings</span><span class="p">:</span>
<span class="w">    </span><span class="sd">"""Options for instrumenting models and agents with OpenTelemetry.</span>

<span class="sd">    Used in:</span>

<span class="sd">    - `Agent(instrument=...)`</span>
<span class="sd">    - [`Agent.instrument_all()`][pydantic_ai.agent.Agent.instrument_all]</span>
<span class="sd">    - [`InstrumentedModel`][pydantic_ai.models.instrumented.InstrumentedModel]</span>

<span class="sd">    See the [Debugging and Monitoring guide](https://ai.pydantic.dev/logfire/) for more info.</span>
<span class="sd">    """</span>

    <span class="n">tracer</span><span class="p">:</span> <span class="n">Tracer</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="nb">repr</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
    <span class="n">event_logger</span><span class="p">:</span> <span class="n">EventLogger</span> <span class="o">=</span> <span class="n">field</span><span class="p">(</span><span class="nb">repr</span><span class="o">=</span><span class="kc">False</span><span class="p">)</span>
    <span class="n">event_mode</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'attributes'</span><span class="p">,</span> <span class="s1">'logs'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'attributes'</span>

    <span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="o">*</span><span class="p">,</span>
        <span class="n">event_mode</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'attributes'</span><span class="p">,</span> <span class="s1">'logs'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'attributes'</span><span class="p">,</span>
        <span class="n">tracer_provider</span><span class="p">:</span> <span class="n">TracerProvider</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">event_logger_provider</span><span class="p">:</span> <span class="n">EventLoggerProvider</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">):</span>
<span class="w">        </span><span class="sd">"""Create instrumentation options.</span>

<span class="sd">        Args:</span>
<span class="sd">            event_mode: The mode for emitting events. If `'attributes'`, events are attached to the span as attributes.</span>
<span class="sd">                If `'logs'`, events are emitted as OpenTelemetry log-based events.</span>
<span class="sd">            tracer_provider: The OpenTelemetry tracer provider to use.</span>
<span class="sd">                If not provided, the global tracer provider is used.</span>
<span class="sd">                Calling `logfire.configure()` sets the global tracer provider, so most users don't need this.</span>
<span class="sd">            event_logger_provider: The OpenTelemetry event logger provider to use.</span>
<span class="sd">                If not provided, the global event logger provider is used.</span>
<span class="sd">                Calling `logfire.configure()` sets the global event logger provider, so most users don't need this.</span>
<span class="sd">                This is only used if `event_mode='logs'`.</span>
<span class="sd">        """</span>
        <span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">__version__</span>

        <span class="n">tracer_provider</span> <span class="o">=</span> <span class="n">tracer_provider</span> <span class="ow">or</span> <span class="n">get_tracer_provider</span><span class="p">()</span>
        <span class="n">event_logger_provider</span> <span class="o">=</span> <span class="n">event_logger_provider</span> <span class="ow">or</span> <span class="n">get_event_logger_provider</span><span class="p">()</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="o">=</span> <span class="n">tracer_provider</span><span class="o">.</span><span class="n">get_tracer</span><span class="p">(</span><span class="s1">'pydantic-ai'</span><span class="p">,</span> <span class="n">__version__</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">event_logger</span> <span class="o">=</span> <span class="n">event_logger_provider</span><span class="o">.</span><span class="n">get_event_logger</span><span class="p">(</span><span class="s1">'pydantic-ai'</span><span class="p">,</span> <span class="n">__version__</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">event_mode</span> <span class="o">=</span> <span class="n">event_mode</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-function">


<h4 id="pydantic_ai.models.instrumented.InstrumentationSettings.__init__" class="doc doc-heading">
            <span class="doc doc-object-name doc-function-name">__init__</span>


</h4>
<div class="language-python doc-signature highlight"><pre id="__code_1"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_1 > code"></button><code><span class="fm">__init__</span><span class="p">(</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="nf">event_mode</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a></span><span class="p">[</span>
        <span class="s2">"attributes"</span><span class="p">,</span> <span class="s2">"logs"</span>
    <span class="p">]</span> <span class="o">=</span> <span class="s2">"attributes"</span><span class="p">,</span>
    <span class="n">tracer_provider</span><span class="p">:</span> <span class="n"><span title="opentelemetry.trace.TracerProvider">TracerProvider</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">event_logger_provider</span><span class="p">:</span> <span class="n"><span title="opentelemetry._events.EventLoggerProvider">EventLoggerProvider</span></span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
<span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Create instrumentation options.</p>


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
                <code>event_mode</code>
            </td>
            <td>
                  <code><a class="autorefs autorefs-external" title="typing.Literal" href="https://docs.python.org/3/library/typing.html#typing.Literal">Literal</a>['attributes', 'logs']</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The mode for emitting events. If <code>'attributes'</code>, events are attached to the span as attributes.
If <code>'logs'</code>, events are emitted as OpenTelemetry log-based events.</p>
              </div>
            </td>
            <td>
                  <code>'attributes'</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>tracer_provider</code>
            </td>
            <td>
                  <code><span title="opentelemetry.trace.TracerProvider">TracerProvider</span> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The OpenTelemetry tracer provider to use.
If not provided, the global tracer provider is used.
Calling <code>logfire.configure()</code> sets the global tracer provider, so most users don't need this.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
          <tr class="doc-section-item">
            <td>
                <code>event_logger_provider</code>
            </td>
            <td>
                  <code><span title="opentelemetry._events.EventLoggerProvider">EventLoggerProvider</span> | None</code>
            </td>
            <td>
              <div class="doc-md-description">
                <p>The OpenTelemetry event logger provider to use.
If not provided, the global event logger provider is used.
Calling <code>logfire.configure()</code> sets the global event logger provider, so most users don't need this.
This is only used if <code>event_mode='logs'</code>.</p>
              </div>
            </td>
            <td>
                  <code>None</code>
            </td>
          </tr>
      </tbody>
    </table></div></div>

            <details class="quote">
              <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/models/instrumented.py</code></summary>
              <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">69</span>
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
<span class="normal">88</span>
<span class="normal">89</span>
<span class="normal">90</span>
<span class="normal">91</span>
<span class="normal">92</span>
<span class="normal">93</span>
<span class="normal">94</span>
<span class="normal">95</span></pre></div></td><td class="code"><div><pre id="__code_2"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_2 > code"></button><code tabindex="0"><span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
    <span class="bp">self</span><span class="p">,</span>
    <span class="o">*</span><span class="p">,</span>
    <span class="n">event_mode</span><span class="p">:</span> <span class="n">Literal</span><span class="p">[</span><span class="s1">'attributes'</span><span class="p">,</span> <span class="s1">'logs'</span><span class="p">]</span> <span class="o">=</span> <span class="s1">'attributes'</span><span class="p">,</span>
    <span class="n">tracer_provider</span><span class="p">:</span> <span class="n">TracerProvider</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="n">event_logger_provider</span><span class="p">:</span> <span class="n">EventLoggerProvider</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
<span class="p">):</span>
<span class="w">    </span><span class="sd">"""Create instrumentation options.</span>

<span class="sd">    Args:</span>
<span class="sd">        event_mode: The mode for emitting events. If `'attributes'`, events are attached to the span as attributes.</span>
<span class="sd">            If `'logs'`, events are emitted as OpenTelemetry log-based events.</span>
<span class="sd">        tracer_provider: The OpenTelemetry tracer provider to use.</span>
<span class="sd">            If not provided, the global tracer provider is used.</span>
<span class="sd">            Calling `logfire.configure()` sets the global tracer provider, so most users don't need this.</span>
<span class="sd">        event_logger_provider: The OpenTelemetry event logger provider to use.</span>
<span class="sd">            If not provided, the global event logger provider is used.</span>
<span class="sd">            Calling `logfire.configure()` sets the global event logger provider, so most users don't need this.</span>
<span class="sd">            This is only used if `event_mode='logs'`.</span>
<span class="sd">    """</span>
    <span class="kn">from</span><span class="w"> </span><span class="nn">pydantic_ai</span><span class="w"> </span><span class="kn">import</span> <span class="n">__version__</span>

    <span class="n">tracer_provider</span> <span class="o">=</span> <span class="n">tracer_provider</span> <span class="ow">or</span> <span class="n">get_tracer_provider</span><span class="p">()</span>
    <span class="n">event_logger_provider</span> <span class="o">=</span> <span class="n">event_logger_provider</span> <span class="ow">or</span> <span class="n">get_event_logger_provider</span><span class="p">()</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">tracer</span> <span class="o">=</span> <span class="n">tracer_provider</span><span class="o">.</span><span class="n">get_tracer</span><span class="p">(</span><span class="s1">'pydantic-ai'</span><span class="p">,</span> <span class="n">__version__</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">event_logger</span> <span class="o">=</span> <span class="n">event_logger_provider</span><span class="o">.</span><span class="n">get_event_logger</span><span class="p">(</span><span class="s1">'pydantic-ai'</span><span class="p">,</span> <span class="n">__version__</span><span class="p">)</span>
    <span class="bp">self</span><span class="o">.</span><span class="n">event_mode</span> <span class="o">=</span> <span class="n">event_mode</span>
</code></pre></div></td></tr></tbody></table></div>
            </details>
    </div>

</div>




  </div>

    </div>

</div>






<div class="doc doc-object doc-class">



<h3 id="pydantic_ai.models.instrumented.InstrumentedModel" class="doc doc-heading">
            <span class="doc doc-object-name doc-class-name">InstrumentedModel</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-dataclass"><code>dataclass</code></small>
  </span>

</h3>


    <div class="doc doc-contents ">
            <p class="doc doc-class-bases">
              Bases: <code><a class="autorefs autorefs-internal" title="pydantic_ai.models.wrapper.WrapperModel" href="../wrapper/#pydantic_ai.models.wrapper.WrapperModel">WrapperModel</a></code></p>


        <p>Model which wraps another model so that requests are instrumented with OpenTelemetry.</p>
<p>See the <a href="https://ai.pydantic.dev/logfire/">Debugging and Monitoring guide</a> for more info.</p>






              <details class="quote">
                <summary>Source code in <code>pydantic_ai_slim/pydantic_ai/models/instrumented.py</code></summary>
                <div class="language-python highlight"><table class="highlighttable"><tbody><tr><td class="linenos"><div class="linenodiv"><pre><span></span><span class="normal">102</span>
<span class="normal">103</span>
<span class="normal">104</span>
<span class="normal">105</span>
<span class="normal">106</span>
<span class="normal">107</span>
<span class="normal">108</span>
<span class="normal">109</span>
<span class="normal">110</span>
<span class="normal">111</span>
<span class="normal">112</span>
<span class="normal">113</span>
<span class="normal">114</span>
<span class="normal">115</span>
<span class="normal">116</span>
<span class="normal">117</span>
<span class="normal">118</span>
<span class="normal">119</span>
<span class="normal">120</span>
<span class="normal">121</span>
<span class="normal">122</span>
<span class="normal">123</span>
<span class="normal">124</span>
<span class="normal">125</span>
<span class="normal">126</span>
<span class="normal">127</span>
<span class="normal">128</span>
<span class="normal">129</span>
<span class="normal">130</span>
<span class="normal">131</span>
<span class="normal">132</span>
<span class="normal">133</span>
<span class="normal">134</span>
<span class="normal">135</span>
<span class="normal">136</span>
<span class="normal">137</span>
<span class="normal">138</span>
<span class="normal">139</span>
<span class="normal">140</span>
<span class="normal">141</span>
<span class="normal">142</span>
<span class="normal">143</span>
<span class="normal">144</span>
<span class="normal">145</span>
<span class="normal">146</span>
<span class="normal">147</span>
<span class="normal">148</span>
<span class="normal">149</span>
<span class="normal">150</span>
<span class="normal">151</span>
<span class="normal">152</span>
<span class="normal">153</span>
<span class="normal">154</span>
<span class="normal">155</span>
<span class="normal">156</span>
<span class="normal">157</span>
<span class="normal">158</span>
<span class="normal">159</span>
<span class="normal">160</span>
<span class="normal">161</span>
<span class="normal">162</span>
<span class="normal">163</span>
<span class="normal">164</span>
<span class="normal">165</span>
<span class="normal">166</span>
<span class="normal">167</span>
<span class="normal">168</span>
<span class="normal">169</span>
<span class="normal">170</span>
<span class="normal">171</span>
<span class="normal">172</span>
<span class="normal">173</span>
<span class="normal">174</span>
<span class="normal">175</span>
<span class="normal">176</span>
<span class="normal">177</span>
<span class="normal">178</span>
<span class="normal">179</span>
<span class="normal">180</span>
<span class="normal">181</span>
<span class="normal">182</span>
<span class="normal">183</span>
<span class="normal">184</span>
<span class="normal">185</span>
<span class="normal">186</span>
<span class="normal">187</span>
<span class="normal">188</span>
<span class="normal">189</span>
<span class="normal">190</span>
<span class="normal">191</span>
<span class="normal">192</span>
<span class="normal">193</span>
<span class="normal">194</span>
<span class="normal">195</span>
<span class="normal">196</span>
<span class="normal">197</span>
<span class="normal">198</span>
<span class="normal">199</span>
<span class="normal">200</span>
<span class="normal">201</span>
<span class="normal">202</span>
<span class="normal">203</span>
<span class="normal">204</span>
<span class="normal">205</span>
<span class="normal">206</span>
<span class="normal">207</span>
<span class="normal">208</span>
<span class="normal">209</span>
<span class="normal">210</span>
<span class="normal">211</span>
<span class="normal">212</span>
<span class="normal">213</span>
<span class="normal">214</span>
<span class="normal">215</span>
<span class="normal">216</span>
<span class="normal">217</span>
<span class="normal">218</span>
<span class="normal">219</span>
<span class="normal">220</span>
<span class="normal">221</span>
<span class="normal">222</span>
<span class="normal">223</span>
<span class="normal">224</span>
<span class="normal">225</span>
<span class="normal">226</span>
<span class="normal">227</span>
<span class="normal">228</span>
<span class="normal">229</span>
<span class="normal">230</span>
<span class="normal">231</span>
<span class="normal">232</span>
<span class="normal">233</span>
<span class="normal">234</span>
<span class="normal">235</span>
<span class="normal">236</span>
<span class="normal">237</span>
<span class="normal">238</span>
<span class="normal">239</span>
<span class="normal">240</span>
<span class="normal">241</span>
<span class="normal">242</span>
<span class="normal">243</span>
<span class="normal">244</span>
<span class="normal">245</span>
<span class="normal">246</span>
<span class="normal">247</span>
<span class="normal">248</span>
<span class="normal">249</span>
<span class="normal">250</span>
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
<span class="normal">290</span></pre></div></td><td class="code"><div><pre id="__code_3"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_3 > code"></button><code tabindex="0"><span class="nd">@dataclass</span>
<span class="k">class</span><span class="w"> </span><span class="nc">InstrumentedModel</span><span class="p">(</span><span class="n">WrapperModel</span><span class="p">):</span>
<span class="w">    </span><span class="sd">"""Model which wraps another model so that requests are instrumented with OpenTelemetry.</span>

<span class="sd">    See the [Debugging and Monitoring guide](https://ai.pydantic.dev/logfire/) for more info.</span>
<span class="sd">    """</span>

    <span class="n">settings</span><span class="p">:</span> <span class="n">InstrumentationSettings</span>
<span class="w">    </span><span class="sd">"""Configuration for instrumenting requests."""</span>

    <span class="k">def</span><span class="w"> </span><span class="fm">__init__</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">wrapped</span><span class="p">:</span> <span class="n">Model</span> <span class="o">|</span> <span class="n">KnownModelName</span><span class="p">,</span>
        <span class="n">options</span><span class="p">:</span> <span class="n">InstrumentationSettings</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="fm">__init__</span><span class="p">(</span><span class="n">wrapped</span><span class="p">)</span>
        <span class="bp">self</span><span class="o">.</span><span class="n">settings</span> <span class="o">=</span> <span class="n">options</span> <span class="ow">or</span> <span class="n">InstrumentationSettings</span><span class="p">()</span>

    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">request</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">messages</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ModelMessage</span><span class="p">],</span>
        <span class="n">model_settings</span><span class="p">:</span> <span class="n">ModelSettings</span> <span class="o">|</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">model_request_parameters</span><span class="p">:</span> <span class="n">ModelRequestParameters</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">tuple</span><span class="p">[</span><span class="n">ModelResponse</span><span class="p">,</span> <span class="n">Usage</span><span class="p">]:</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_instrument</span><span class="p">(</span><span class="n">messages</span><span class="p">,</span> <span class="n">model_settings</span><span class="p">,</span> <span class="n">model_request_parameters</span><span class="p">)</span> <span class="k">as</span> <span class="n">finish</span><span class="p">:</span>
            <span class="n">response</span><span class="p">,</span> <span class="n">usage</span> <span class="o">=</span> <span class="k">await</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">request</span><span class="p">(</span><span class="n">messages</span><span class="p">,</span> <span class="n">model_settings</span><span class="p">,</span> <span class="n">model_request_parameters</span><span class="p">)</span>
            <span class="n">finish</span><span class="p">(</span><span class="n">response</span><span class="p">,</span> <span class="n">usage</span><span class="p">)</span>
            <span class="k">return</span> <span class="n">response</span><span class="p">,</span> <span class="n">usage</span>

    <span class="nd">@asynccontextmanager</span>
    <span class="k">async</span> <span class="k">def</span><span class="w"> </span><span class="nf">request_stream</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">messages</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ModelMessage</span><span class="p">],</span>
        <span class="n">model_settings</span><span class="p">:</span> <span class="n">ModelSettings</span> <span class="o">|</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">model_request_parameters</span><span class="p">:</span> <span class="n">ModelRequestParameters</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">AsyncIterator</span><span class="p">[</span><span class="n">StreamedResponse</span><span class="p">]:</span>
        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">_instrument</span><span class="p">(</span><span class="n">messages</span><span class="p">,</span> <span class="n">model_settings</span><span class="p">,</span> <span class="n">model_request_parameters</span><span class="p">)</span> <span class="k">as</span> <span class="n">finish</span><span class="p">:</span>
            <span class="n">response_stream</span><span class="p">:</span> <span class="n">StreamedResponse</span> <span class="o">|</span> <span class="kc">None</span> <span class="o">=</span> <span class="kc">None</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="k">async</span> <span class="k">with</span> <span class="nb">super</span><span class="p">()</span><span class="o">.</span><span class="n">request_stream</span><span class="p">(</span>
                    <span class="n">messages</span><span class="p">,</span> <span class="n">model_settings</span><span class="p">,</span> <span class="n">model_request_parameters</span>
                <span class="p">)</span> <span class="k">as</span> <span class="n">response_stream</span><span class="p">:</span>
                    <span class="k">yield</span> <span class="n">response_stream</span>
            <span class="k">finally</span><span class="p">:</span>
                <span class="k">if</span> <span class="n">response_stream</span><span class="p">:</span>
                    <span class="n">finish</span><span class="p">(</span><span class="n">response_stream</span><span class="o">.</span><span class="n">get</span><span class="p">(),</span> <span class="n">response_stream</span><span class="o">.</span><span class="n">usage</span><span class="p">())</span>

    <span class="nd">@contextmanager</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">_instrument</span><span class="p">(</span>
        <span class="bp">self</span><span class="p">,</span>
        <span class="n">messages</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ModelMessage</span><span class="p">],</span>
        <span class="n">model_settings</span><span class="p">:</span> <span class="n">ModelSettings</span> <span class="o">|</span> <span class="kc">None</span><span class="p">,</span>
        <span class="n">model_request_parameters</span><span class="p">:</span> <span class="n">ModelRequestParameters</span><span class="p">,</span>
    <span class="p">)</span> <span class="o">-&gt;</span> <span class="n">Iterator</span><span class="p">[</span><span class="n">Callable</span><span class="p">[[</span><span class="n">ModelResponse</span><span class="p">,</span> <span class="n">Usage</span><span class="p">],</span> <span class="kc">None</span><span class="p">]]:</span>
        <span class="n">operation</span> <span class="o">=</span> <span class="s1">'chat'</span>
        <span class="n">span_name</span> <span class="o">=</span> <span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="n">operation</span><span class="si">}</span><span class="s1"> </span><span class="si">{</span><span class="bp">self</span><span class="o">.</span><span class="n">model_name</span><span class="si">}</span><span class="s1">'</span>
        <span class="c1"># TODO Missing attributes:</span>
        <span class="c1">#  - error.type: unclear if we should do something here or just always rely on span exceptions</span>
        <span class="c1">#  - gen_ai.request.stop_sequences/top_k: model_settings doesn't include these</span>
        <span class="n">attributes</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">AttributeValue</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span>
            <span class="s1">'gen_ai.operation.name'</span><span class="p">:</span> <span class="n">operation</span><span class="p">,</span>
            <span class="o">**</span><span class="bp">self</span><span class="o">.</span><span class="n">model_attributes</span><span class="p">(</span><span class="bp">self</span><span class="o">.</span><span class="n">wrapped</span><span class="p">),</span>
            <span class="s1">'model_request_parameters'</span><span class="p">:</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span><span class="n">InstrumentedModel</span><span class="o">.</span><span class="n">serialize_any</span><span class="p">(</span><span class="n">model_request_parameters</span><span class="p">)),</span>
            <span class="s1">'logfire.json_schema'</span><span class="p">:</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span>
                <span class="p">{</span>
                    <span class="s1">'type'</span><span class="p">:</span> <span class="s1">'object'</span><span class="p">,</span>
                    <span class="s1">'properties'</span><span class="p">:</span> <span class="p">{</span><span class="s1">'model_request_parameters'</span><span class="p">:</span> <span class="p">{</span><span class="s1">'type'</span><span class="p">:</span> <span class="s1">'object'</span><span class="p">}},</span>
                <span class="p">}</span>
            <span class="p">),</span>
        <span class="p">}</span>

        <span class="k">if</span> <span class="n">model_settings</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">key</span> <span class="ow">in</span> <span class="n">MODEL_SETTING_ATTRIBUTES</span><span class="p">:</span>
                <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">value</span> <span class="o">:=</span> <span class="n">model_settings</span><span class="o">.</span><span class="n">get</span><span class="p">(</span><span class="n">key</span><span class="p">),</span> <span class="p">(</span><span class="nb">float</span><span class="p">,</span> <span class="nb">int</span><span class="p">)):</span>
                    <span class="n">attributes</span><span class="p">[</span><span class="sa">f</span><span class="s1">'gen_ai.request.</span><span class="si">{</span><span class="n">key</span><span class="si">}</span><span class="s1">'</span><span class="p">]</span> <span class="o">=</span> <span class="n">value</span>

        <span class="k">with</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">tracer</span><span class="o">.</span><span class="n">start_as_current_span</span><span class="p">(</span><span class="n">span_name</span><span class="p">,</span> <span class="n">attributes</span><span class="o">=</span><span class="n">attributes</span><span class="p">)</span> <span class="k">as</span> <span class="n">span</span><span class="p">:</span>

            <span class="k">def</span><span class="w"> </span><span class="nf">finish</span><span class="p">(</span><span class="n">response</span><span class="p">:</span> <span class="n">ModelResponse</span><span class="p">,</span> <span class="n">usage</span><span class="p">:</span> <span class="n">Usage</span><span class="p">):</span>
                <span class="k">if</span> <span class="ow">not</span> <span class="n">span</span><span class="o">.</span><span class="n">is_recording</span><span class="p">():</span>
                    <span class="k">return</span>

                <span class="n">events</span> <span class="o">=</span> <span class="bp">self</span><span class="o">.</span><span class="n">messages_to_otel_events</span><span class="p">(</span><span class="n">messages</span><span class="p">)</span>
                <span class="k">for</span> <span class="n">event</span> <span class="ow">in</span> <span class="bp">self</span><span class="o">.</span><span class="n">messages_to_otel_events</span><span class="p">([</span><span class="n">response</span><span class="p">]):</span>
                    <span class="n">events</span><span class="o">.</span><span class="n">append</span><span class="p">(</span>
                        <span class="n">Event</span><span class="p">(</span>
                            <span class="s1">'gen_ai.choice'</span><span class="p">,</span>
                            <span class="n">body</span><span class="o">=</span><span class="p">{</span>
                                <span class="c1"># TODO finish_reason</span>
                                <span class="s1">'index'</span><span class="p">:</span> <span class="mi">0</span><span class="p">,</span>
                                <span class="s1">'message'</span><span class="p">:</span> <span class="n">event</span><span class="o">.</span><span class="n">body</span><span class="p">,</span>
                            <span class="p">},</span>
                        <span class="p">)</span>
                    <span class="p">)</span>
                <span class="n">new_attributes</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">AttributeValue</span><span class="p">]</span> <span class="o">=</span> <span class="n">usage</span><span class="o">.</span><span class="n">opentelemetry_attributes</span><span class="p">()</span>  <span class="c1"># type: ignore</span>
                <span class="n">attributes</span><span class="o">.</span><span class="n">update</span><span class="p">(</span><span class="nb">getattr</span><span class="p">(</span><span class="n">span</span><span class="p">,</span> <span class="s1">'attributes'</span><span class="p">,</span> <span class="p">{}))</span>
                <span class="n">request_model</span> <span class="o">=</span> <span class="n">attributes</span><span class="p">[</span><span class="n">GEN_AI_REQUEST_MODEL_ATTRIBUTE</span><span class="p">]</span>
                <span class="n">new_attributes</span><span class="p">[</span><span class="s1">'gen_ai.response.model'</span><span class="p">]</span> <span class="o">=</span> <span class="n">response</span><span class="o">.</span><span class="n">model_name</span> <span class="ow">or</span> <span class="n">request_model</span>
                <span class="n">span</span><span class="o">.</span><span class="n">set_attributes</span><span class="p">(</span><span class="n">new_attributes</span><span class="p">)</span>
                <span class="n">span</span><span class="o">.</span><span class="n">update_name</span><span class="p">(</span><span class="sa">f</span><span class="s1">'</span><span class="si">{</span><span class="n">operation</span><span class="si">}</span><span class="s1"> </span><span class="si">{</span><span class="n">request_model</span><span class="si">}</span><span class="s1">'</span><span class="p">)</span>
                <span class="k">for</span> <span class="n">event</span> <span class="ow">in</span> <span class="n">events</span><span class="p">:</span>
                    <span class="n">event</span><span class="o">.</span><span class="n">attributes</span> <span class="o">=</span> <span class="p">{</span>
                        <span class="n">GEN_AI_SYSTEM_ATTRIBUTE</span><span class="p">:</span> <span class="n">attributes</span><span class="p">[</span><span class="n">GEN_AI_SYSTEM_ATTRIBUTE</span><span class="p">],</span>
                        <span class="o">**</span><span class="p">(</span><span class="n">event</span><span class="o">.</span><span class="n">attributes</span> <span class="ow">or</span> <span class="p">{}),</span>
                    <span class="p">}</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">_emit_events</span><span class="p">(</span><span class="n">span</span><span class="p">,</span> <span class="n">events</span><span class="p">)</span>

            <span class="k">yield</span> <span class="n">finish</span>

    <span class="k">def</span><span class="w"> </span><span class="nf">_emit_events</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">span</span><span class="p">:</span> <span class="n">Span</span><span class="p">,</span> <span class="n">events</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">Event</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="kc">None</span><span class="p">:</span>
        <span class="k">if</span> <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">event_mode</span> <span class="o">==</span> <span class="s1">'logs'</span><span class="p">:</span>
            <span class="k">for</span> <span class="n">event</span> <span class="ow">in</span> <span class="n">events</span><span class="p">:</span>
                <span class="bp">self</span><span class="o">.</span><span class="n">settings</span><span class="o">.</span><span class="n">event_logger</span><span class="o">.</span><span class="n">emit</span><span class="p">(</span><span class="n">event</span><span class="p">)</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">attr_name</span> <span class="o">=</span> <span class="s1">'events'</span>
            <span class="n">span</span><span class="o">.</span><span class="n">set_attributes</span><span class="p">(</span>
                <span class="p">{</span>
                    <span class="n">attr_name</span><span class="p">:</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">([</span><span class="bp">self</span><span class="o">.</span><span class="n">event_to_dict</span><span class="p">(</span><span class="n">event</span><span class="p">)</span> <span class="k">for</span> <span class="n">event</span> <span class="ow">in</span> <span class="n">events</span><span class="p">]),</span>
                    <span class="s1">'logfire.json_schema'</span><span class="p">:</span> <span class="n">json</span><span class="o">.</span><span class="n">dumps</span><span class="p">(</span>
                        <span class="p">{</span>
                            <span class="s1">'type'</span><span class="p">:</span> <span class="s1">'object'</span><span class="p">,</span>
                            <span class="s1">'properties'</span><span class="p">:</span> <span class="p">{</span>
                                <span class="n">attr_name</span><span class="p">:</span> <span class="p">{</span><span class="s1">'type'</span><span class="p">:</span> <span class="s1">'array'</span><span class="p">},</span>
                                <span class="s1">'model_request_parameters'</span><span class="p">:</span> <span class="p">{</span><span class="s1">'type'</span><span class="p">:</span> <span class="s1">'object'</span><span class="p">},</span>
                            <span class="p">},</span>
                        <span class="p">}</span>
                    <span class="p">),</span>
                <span class="p">}</span>
            <span class="p">)</span>

    <span class="nd">@staticmethod</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">model_attributes</span><span class="p">(</span><span class="n">model</span><span class="p">:</span> <span class="n">Model</span><span class="p">):</span>
        <span class="n">attributes</span><span class="p">:</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">AttributeValue</span><span class="p">]</span> <span class="o">=</span> <span class="p">{</span>
            <span class="n">GEN_AI_SYSTEM_ATTRIBUTE</span><span class="p">:</span> <span class="n">model</span><span class="o">.</span><span class="n">system</span><span class="p">,</span>
            <span class="n">GEN_AI_REQUEST_MODEL_ATTRIBUTE</span><span class="p">:</span> <span class="n">model</span><span class="o">.</span><span class="n">model_name</span><span class="p">,</span>
        <span class="p">}</span>
        <span class="k">if</span> <span class="n">base_url</span> <span class="o">:=</span> <span class="n">model</span><span class="o">.</span><span class="n">base_url</span><span class="p">:</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="n">parsed</span> <span class="o">=</span> <span class="n">urlparse</span><span class="p">(</span><span class="n">base_url</span><span class="p">)</span>
            <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>  <span class="c1"># pragma: no cover</span>
                <span class="k">pass</span>
            <span class="k">else</span><span class="p">:</span>
                <span class="k">if</span> <span class="n">parsed</span><span class="o">.</span><span class="n">hostname</span><span class="p">:</span>
                    <span class="n">attributes</span><span class="p">[</span><span class="s1">'server.address'</span><span class="p">]</span> <span class="o">=</span> <span class="n">parsed</span><span class="o">.</span><span class="n">hostname</span>
                <span class="k">if</span> <span class="n">parsed</span><span class="o">.</span><span class="n">port</span><span class="p">:</span>
                    <span class="n">attributes</span><span class="p">[</span><span class="s1">'server.port'</span><span class="p">]</span> <span class="o">=</span> <span class="n">parsed</span><span class="o">.</span><span class="n">port</span>

        <span class="k">return</span> <span class="n">attributes</span>

    <span class="nd">@staticmethod</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">event_to_dict</span><span class="p">(</span><span class="n">event</span><span class="p">:</span> <span class="n">Event</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">dict</span><span class="p">[</span><span class="nb">str</span><span class="p">,</span> <span class="n">Any</span><span class="p">]:</span>
        <span class="k">if</span> <span class="ow">not</span> <span class="n">event</span><span class="o">.</span><span class="n">body</span><span class="p">:</span>
            <span class="n">body</span> <span class="o">=</span> <span class="p">{}</span>
        <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">event</span><span class="o">.</span><span class="n">body</span><span class="p">,</span> <span class="n">Mapping</span><span class="p">):</span>
            <span class="n">body</span> <span class="o">=</span> <span class="n">event</span><span class="o">.</span><span class="n">body</span>  <span class="c1"># type: ignore</span>
        <span class="k">else</span><span class="p">:</span>
            <span class="n">body</span> <span class="o">=</span> <span class="p">{</span><span class="s1">'body'</span><span class="p">:</span> <span class="n">event</span><span class="o">.</span><span class="n">body</span><span class="p">}</span>
        <span class="k">return</span> <span class="p">{</span><span class="o">**</span><span class="n">body</span><span class="p">,</span> <span class="o">**</span><span class="p">(</span><span class="n">event</span><span class="o">.</span><span class="n">attributes</span> <span class="ow">or</span> <span class="p">{})}</span>

    <span class="nd">@staticmethod</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">messages_to_otel_events</span><span class="p">(</span><span class="n">messages</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">ModelMessage</span><span class="p">])</span> <span class="o">-&gt;</span> <span class="nb">list</span><span class="p">[</span><span class="n">Event</span><span class="p">]:</span>
        <span class="n">result</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">Event</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
        <span class="k">for</span> <span class="n">message_index</span><span class="p">,</span> <span class="n">message</span> <span class="ow">in</span> <span class="nb">enumerate</span><span class="p">(</span><span class="n">messages</span><span class="p">):</span>
            <span class="n">message_events</span><span class="p">:</span> <span class="nb">list</span><span class="p">[</span><span class="n">Event</span><span class="p">]</span> <span class="o">=</span> <span class="p">[]</span>
            <span class="k">if</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">message</span><span class="p">,</span> <span class="n">ModelRequest</span><span class="p">):</span>
                <span class="k">for</span> <span class="n">part</span> <span class="ow">in</span> <span class="n">message</span><span class="o">.</span><span class="n">parts</span><span class="p">:</span>
                    <span class="k">if</span> <span class="nb">hasattr</span><span class="p">(</span><span class="n">part</span><span class="p">,</span> <span class="s1">'otel_event'</span><span class="p">):</span>
                        <span class="n">message_events</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="n">part</span><span class="o">.</span><span class="n">otel_event</span><span class="p">())</span>
            <span class="k">elif</span> <span class="nb">isinstance</span><span class="p">(</span><span class="n">message</span><span class="p">,</span> <span class="n">ModelResponse</span><span class="p">):</span>
                <span class="n">message_events</span> <span class="o">=</span> <span class="n">message</span><span class="o">.</span><span class="n">otel_events</span><span class="p">()</span>
            <span class="k">for</span> <span class="n">event</span> <span class="ow">in</span> <span class="n">message_events</span><span class="p">:</span>
                <span class="n">event</span><span class="o">.</span><span class="n">attributes</span> <span class="o">=</span> <span class="p">{</span>
                    <span class="s1">'gen_ai.message.index'</span><span class="p">:</span> <span class="n">message_index</span><span class="p">,</span>
                    <span class="o">**</span><span class="p">(</span><span class="n">event</span><span class="o">.</span><span class="n">attributes</span> <span class="ow">or</span> <span class="p">{}),</span>
                <span class="p">}</span>
            <span class="n">result</span><span class="o">.</span><span class="n">extend</span><span class="p">(</span><span class="n">message_events</span><span class="p">)</span>
        <span class="k">for</span> <span class="n">event</span> <span class="ow">in</span> <span class="n">result</span><span class="p">:</span>
            <span class="n">event</span><span class="o">.</span><span class="n">body</span> <span class="o">=</span> <span class="n">InstrumentedModel</span><span class="o">.</span><span class="n">serialize_any</span><span class="p">(</span><span class="n">event</span><span class="o">.</span><span class="n">body</span><span class="p">)</span>
        <span class="k">return</span> <span class="n">result</span>

    <span class="nd">@staticmethod</span>
    <span class="k">def</span><span class="w"> </span><span class="nf">serialize_any</span><span class="p">(</span><span class="n">value</span><span class="p">:</span> <span class="n">Any</span><span class="p">)</span> <span class="o">-&gt;</span> <span class="nb">str</span><span class="p">:</span>
        <span class="k">try</span><span class="p">:</span>
            <span class="k">return</span> <span class="n">ANY_ADAPTER</span><span class="o">.</span><span class="n">dump_python</span><span class="p">(</span><span class="n">value</span><span class="p">,</span> <span class="n">mode</span><span class="o">=</span><span class="s1">'json'</span><span class="p">)</span>
        <span class="k">except</span> <span class="ne">Exception</span><span class="p">:</span>
            <span class="k">try</span><span class="p">:</span>
                <span class="k">return</span> <span class="nb">str</span><span class="p">(</span><span class="n">value</span><span class="p">)</span>
            <span class="k">except</span> <span class="ne">Exception</span> <span class="k">as</span> <span class="n">e</span><span class="p">:</span>
                <span class="k">return</span> <span class="sa">f</span><span class="s1">'Unable to serialize: </span><span class="si">{</span><span class="n">e</span><span class="si">}</span><span class="s1">'</span>
</code></pre></div></td></tr></tbody></table></div>
              </details>



  <div class="doc doc-children">







<div class="doc doc-object doc-attribute">



<h4 id="pydantic_ai.models.instrumented.InstrumentedModel.settings" class="doc doc-heading">
            <span class="doc doc-object-name doc-attribute-name">settings</span>


  <span class="doc doc-labels">
      <small class="doc doc-label doc-label-instance-attribute"><code>instance-attribute</code></small>
  </span>

</h4>
<div class="language-python doc-signature highlight"><pre id="__code_4"><span></span><button class="md-clipboard md-icon" title="Copy to clipboard" data-clipboard-target="#__code_4 > code"></button><code><span class="n">settings</span><span class="p">:</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.instrumented.InstrumentationSettings" href="#pydantic_ai.models.instrumented.InstrumentationSettings">InstrumentationSettings</a></span> <span class="o">=</span> <span class="p">(</span>
    <span class="n"><span title="pydantic_ai.models.instrumented.InstrumentedModel(options)">options</span></span> <span class="ow">or</span> <span class="n"><a class="autorefs autorefs-internal" title="pydantic_ai.models.instrumented.InstrumentationSettings" href="#pydantic_ai.models.instrumented.InstrumentationSettings">InstrumentationSettings</a></span><span class="p">()</span>
<span class="p">)</span>
</code></pre></div>

    <div class="doc doc-contents ">

        <p>Configuration for instrumenting requests.</p>
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